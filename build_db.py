from langchain_chroma import Chroma
from dotenv import load_dotenv
import pandas as pd
from typing import List
from langchain.embeddings.base import Embeddings
from sentence_transformers import SentenceTransformer

from app.model.sentence_tranformer_embeddings import SentenceTransformerEmbeddings

quran = pd.read_csv("csv/quran-dataset.csv")
quran
#%%
ids = quran["id"].astype(str).tolist()
texts = quran["en_translation"].tolist()
metadata = quran.apply(
    lambda x: {
        "id": x["id"],
        "arabic": x["arabic"],
        "en_translation": x["en_translation"],
        "surah": x["surah"],
        "surah_no": x["surah_no"],
        "ayah_no": x["ayah_no"],
        "juz_no": x["juz_no"],
    },
    axis=1,
).tolist()

DB_PATH = "./db"

db = Chroma.from_texts(texts=texts, metadatas=metadata, embedding=SentenceTransformerEmbeddings("sentence-transformers/all-MiniLM-L6-v2"),
                       persist_directory=DB_PATH)