import ollama

MODEL_NAME = "qwen2.5:7b"

PROMPT_TEMPLATE = """Bạn là trợ lý AI trả lời câu hỏi dựa trên tài liệu được cung cấp.
Chỉ dùng thông tin trong phần "Ngữ cảnh" bên dưới. Nếu không tìm thấy câu trả lời trong ngữ cảnh, hãy nói rõ là không có thông tin.

Ngữ cảnh:
{context}

Câu hỏi: {question}

Trả lời (bằng tiếng Việt, ngắn gọn, rõ ràng):"""

def generate_answer(question, retrieved_chunks):
    context = "\n\n".join(
        f"[Nguồn: {src}]\n{chunk}" for chunk, src in retrieved_chunks
    )
    prompt = PROMPT_TEMPLATE.format(context=context, question=question)

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
    )
    return response["message"]["content"]