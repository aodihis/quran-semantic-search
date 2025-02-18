from langchain_chroma import Chroma


class VectorService:
    def __init__(self, collection: Chroma):
        self._collection = collection

    def query(self, query: str, n_results: int = 10):
        results = self._collection.similarity_search(query, k=n_results)
        return results