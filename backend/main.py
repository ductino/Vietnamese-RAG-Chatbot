from rag.retriever import retrieve
from rag.generator import generate_answer

def main():
    print("Vietnamese RAG Chatbot — gõ 'exit' để thoát")
    while True:
        question = input("\nBạn hỏi: ").strip()
        if question.lower() in ("exit", "quit"):
            break
        chunks = retrieve(question)
        if not chunks:
            print("Không tìm thấy tài liệu liên quan.")
            continue
        answer = generate_answer(question, chunks)
        print(f"\nTrả lời: {answer}")

if __name__ == "__main__":
    main()