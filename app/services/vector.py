from langchain_chroma import Chroma


class VectorService:
    def __init__(self, collection: Chroma):
        self._collection = collection

    def query(self, query: str, n_results: int = 10):
        results = self._collection.similarity_search(query, k=n_results)
        ret = []
        for result in results:
            print(result.metadata)
            ret.append({
                'arabic': result.metadata['arabic'],
                'verse_no': result.metadata['ayah_no'],
                'en_translation': result.metadata['en_translation'],
                'juz_no': result.metadata['juz_no'],
                'surah': result.metadata['surah'],
                'surah_no': result.metadata['surah_no'],
            })
        return ret