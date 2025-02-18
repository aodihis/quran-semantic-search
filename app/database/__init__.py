import os

from langchain_chroma import Chroma
from app.model.sentence_tranformer_embeddings import SentenceTransformerEmbeddings


def init_chroma():
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    persist_dir = os.path.join(root_dir, 'db')

    client = Chroma(
        persist_directory=persist_dir,
        embedding_function=SentenceTransformerEmbeddings("sentence-transformers/all-MiniLM-L6-v2"),
    )
    return client