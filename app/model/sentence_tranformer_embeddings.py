from sentence_transformers import SentenceTransformer
from typing import List
from chromadb import Embeddings

class SentenceTransformerEmbeddings(Embeddings):
    def __init__(self, model_name: str):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, documents: List[str]):
        return self.model.encode(documents)

    def embed_query(self, query: str):
        return self.model.encode([query])[0]