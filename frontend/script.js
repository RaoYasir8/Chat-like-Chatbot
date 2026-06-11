const API_URL = "http://127.0.0.1:8000/api/chat";

const chatForm = document.getElementById("chatForm");
const userInput = document.getElementById("userInput");
const chatBox = document.getElementById("chatBox");

function addMessage(content, className) {
    const message = document.createElement("div");
    message.className = `message ${className}`;
    message.textContent = content;
    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;
    return message;
}

chatForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const message = userInput.value.trim();
    if (!message) return;

    addMessage(message, "user-message");
    userInput.value = "";

    const loadingMessage = addMessage("Thinking...", "bot-message");
    const submitButton = chatForm.querySelector("button");
    submitButton.disabled = true;

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ message }),
        });

        if (!response.ok) {
            throw new Error("API request failed");
        }

        const data = await response.json();
        loadingMessage.textContent = data.response;
    } catch (error) {
        loadingMessage.textContent = "Sorry, something went wrong. Please try again.";
        loadingMessage.classList.add("error-message");
    } finally {
        submitButton.disabled = false;
        userInput.focus();
    }
});