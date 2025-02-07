from typing import List, Dict, Any, Optional
from .database import Database
from .embeddings import EmbeddingGenerator

class TAG:
    def __init__(self):
        self.db = Database()
        self.embedding_generator = EmbeddingGenerator()
        
    def initialize(self):
        """Initialize the TAG system."""
        self.db.initialize_tables()
        
    def add_knowledge_chunk(self, content: str, domain: str = None) -> int:
        """Add a new knowledge chunk to the system."""
        embedding = self.embedding_generator.generate_embedding(content)
        return self.db.insert_knowledge_chunk(content, embedding, domain)
        
    def create_task(self, name: str, description: str = None,
                    prompt: str = None, domain: str = None) -> int:
        """Create a new task in the system."""
        # Generate embedding from task name and description
        text_to_embed = f"{name} {description if description else ''}"
        embedding = self.embedding_generator.generate_embedding(text_to_embed)
        
        return self.db.create_task(
            name=name,
            embedding=embedding,
            description=description,
            prompt=prompt,
            domain=domain
        )
        
    def get_relevant_knowledge(self, task_id: int, limit: int = 5) -> List[Dict[str, Any]]:
        """Retrieve knowledge chunks relevant to a specific task."""
        return self.db.get_similar_chunks(task_id, limit)
    
    def close(self):
        """Clean up resources."""
        self.db.close() 