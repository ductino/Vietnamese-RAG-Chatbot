import os
from docx import Document as DocxDocument
import chromadb
from sentence_transformers import SentenceTransformer

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOCS_DIR = os.path.join(BASE_DIR, "data", "documents")
VECTOR_DIR = os.path.join(BASE_DIR, "vectorstore")
CHUNK_SIZE = 500       # số ký tự mỗi đoạn
CHUNK_OVERLAP = 50

# Model embedding đa ngôn ngữ, hỗ trợ tiếng Việt tốt
embedder = SentenceTransformer("intfloat/multilingual-e5-base")

def read_file(path):
    if path.endswith(".docx"):
        doc = DocxDocument(path)
        return "\n".join(p.text for p in doc.paragraphs if p.text.strip())
    else:  # .txt, .md
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

def chunk_text(text, size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    chunks = []
    start = 0
    while start < len(text):
        end = start + size
        chunks.append(text[start:end])
        start += size - overlap
    return [c.strip() for c in chunks if c.strip()]

def ingest():
    client = chromadb.PersistentClient(path=VECTOR_DIR)
    collection = client.get_or_create_collection("documents")

    doc_id = 0
    for filename in os.listdir(DOCS_DIR):
        path = os.path.join(DOCS_DIR, filename)
        text = read_file(path)
        chunks = chunk_text(text)

        embeddings = embedder.encode(chunks, normalize_embeddings=True).tolist()
        ids = [f"{filename}_{i}" for i in range(len(chunks))]
        metadatas = [{"source": filename, "chunk_index": i} for i in range(len(chunks))]

        collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=chunks,
            metadatas=metadatas,
        )
        doc_id += len(chunks)
        print(f"Đã nạp {filename}: {len(chunks)} đoạn")

    print(f"Hoàn tất. Tổng {doc_id} đoạn văn bản đã được index.")

if __name__ == "__main__":
    ingest()