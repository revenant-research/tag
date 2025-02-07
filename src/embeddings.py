from typing import List, Union
import openai
import numpy as np
from .config import OPENAI_API_KEY

class EmbeddingGenerator:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY
        
    def generate_embedding(self, text: str) -> List[float]:
        """Generate embedding for a given text using OpenAI's API."""
        response = openai.Embedding.create(
            input=text,
            model="text-embedding-ada-002"
        )
        return response['data'][0]['embedding']
    
    def generate_batch_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for multiple texts in batch."""
        response = openai.Embedding.create(
            input=texts,
            model="text-embedding-ada-002"
        )
        return [data['embedding'] for data in response['data']] 