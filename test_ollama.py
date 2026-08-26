import ollama

response = ollama.chat(
    model="qwen2.5:7b",
    messages=[{"role": "user", "content": "Xin chào, bạn là ai?"}],
)
print(response["message"]["content"])