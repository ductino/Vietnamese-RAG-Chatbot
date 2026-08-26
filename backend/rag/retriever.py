import os
import chromadb
from sentence_transformers import SentenceTransformer

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VECTOR_DIR = os.path.join(BASE_DIR, "vectorstore")
embedder = SentenceTransformer("intfloat/multilingual-e5-base")

def retrieve(query, top_k=4):
    client = chromadb.PersistentClient(path=VECTOR_DIR)
    collection = client.get_collection("documents")

    query_embedding = embedder.encode([query], normalize_embeddings=True).tolist()
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k,
    )

    chunks = results["documents"][0]
    sources = [m["source"] for m in results["metadatas"][0]]
    return list(zip(chunks, sources))