const chatWindow = document.getElementById("chat-window");
const input = document.getElementById("question-input");
const sendBtn = document.getElementById("send-btn");

function addMessage(text, sender, sources = []) {
  const div = document.createElement("div");
  div.className = `message ${sender}`;
  div.textContent = text;

  if (sources.length > 0) {
    const src = document.createElement("span");
    src.className = "sources";
    src.textContent = `Nguồn: ${sources.join(", ")}`;
    div.appendChild(src);
  }

  chatWindow.appendChild(div);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

async function sendMessage() {
  const question = input.value.trim();
  if (!question) return;

  addMessage(question, "user");
  input.value = "";
  sendBtn.disabled = true;

  try {
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question }),
    });
    const data = await res.json();
    addMessage(data.answer, "bot", data.sources);
  } catch (err) {
    addMessage("Lỗi kết nối tới server.", "bot");
  } finally {
    sendBtn.disabled = false;
  }
}

sendBtn.addEventListener("click", sendMessage);
input.addEventListener("keydown", (e) => {
  if (e.key === "Enter") sendMessage();
});