import psycopg2
from psycopg2.extras import execute_values
from pgvector.psycopg2 import register_vector
import numpy as np
from typing import List, Dict, Any
from .config import DB_CONFIG

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(**DB_CONFIG)
        register_vector(self.conn)
        
    def initialize_tables(self):
        """Create the necessary tables and indexes if they don't exist."""
        with self.conn.cursor() as cur:
            # Create extension if not exists
            cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
            
            # Create knowledge_chunks table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS knowledge_chunks (
                    id SERIAL PRIMARY KEY,
                    chunk_content TEXT NOT NULL,
                    domain_name TEXT,
                    chunk_embedding vector(768) NOT NULL,
                    created_at TIMESTAMP DEFAULT NOW()
                );
            """)
            
            # Create tasks table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id SERIAL PRIMARY KEY,
                    task_name TEXT NOT NULL,
                    domain_name TEXT,
                    description TEXT,
                    prompt TEXT,
                    task_embedding vector(768),
                    created_at TIMESTAMP DEFAULT NOW()
                );
            """)
            
            # Create indexes
            cur.execute("""
                CREATE INDEX IF NOT EXISTS knowledge_chunks_embedding_idx 
                ON knowledge_chunks 
                USING ivfflat (chunk_embedding vector_l2_ops)
                WITH (lists = 100);
            """)
            
            cur.execute("""
                CREATE INDEX IF NOT EXISTS tasks_embedding_idx
                ON tasks
                USING ivfflat (task_embedding vector_l2_ops)
                WITH (lists = 50);
            """)
            
        self.conn.commit()

    def insert_knowledge_chunk(self, content: str, embedding: List[float], domain: str = None) -> int:
        """Insert a new knowledge chunk and return its ID."""
        with self.conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO knowledge_chunks (chunk_content, domain_name, chunk_embedding)
                VALUES (%s, %s, %s)
                RETURNING id
                """,
                (content, domain, embedding)
            )
            chunk_id = cur.fetchone()[0]
        self.conn.commit()
        return chunk_id

    def create_task(self, name: str, embedding: List[float], description: str = None,
                    prompt: str = None, domain: str = None) -> int:
        """Create a new task and return its ID."""
        with self.conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO tasks (task_name, domain_name, description, prompt, task_embedding)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id
                """,
                (name, domain, description, prompt, embedding)
            )
            task_id = cur.fetchone()[0]
        self.conn.commit()
        return task_id

    def get_similar_chunks(self, task_id: int, limit: int = 5) -> List[Dict[str, Any]]:
        """Retrieve chunks most similar to a given task."""
        with self.conn.cursor() as cur:
            cur.execute(
                """
                SELECT k.id, k.chunk_content, k.domain_name,
                       k.chunk_embedding <-> t.task_embedding as distance
                FROM knowledge_chunks k, tasks t
                WHERE t.id = %s
                ORDER BY distance
                LIMIT %s
                """,
                (task_id, limit)
            )
            results = cur.fetchall()
            
        return [
            {
                "id": r[0],
                "content": r[1],
                "domain": r[2],
                "distance": r[3]
            }
            for r in results
        ]

    def close(self):
        """Close the database connection."""
        self.conn.close() 