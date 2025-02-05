// chat.js

const chatToggle = document.getElementById('chat-toggle');
const chatWidget = document.getElementById('chat-widget');
const chatClose = document.getElementById('chat-close');
const chatInput = document.getElementById('chat-input');
const chatSend = document.getElementById('chat-send');
const chatMessages = document.getElementById('chat-messages');

// Global array til chat-historik
let conversation = [];

function addMessage(sender, text) {
    const msgContainer = document.createElement('div');
    msgContainer.classList.add('message');
    if (sender === 'You') {
        msgContainer.classList.add('user');
    } else {
        msgContainer.classList.add('coach');
    }
    const bubble = document.createElement('div');
    bubble.classList.add('bubble');
    bubble.innerHTML = text;
    msgContainer.appendChild(bubble);
    chatMessages.appendChild(msgContainer);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function saveChatHistory() {
    localStorage.setItem("chatHistory", JSON.stringify(conversation));
}

function loadChatHistory() {
    const stored = localStorage.getItem("chatHistory");
    if (stored) {
        conversation = JSON.parse(stored);
        conversation.forEach(msg => {
            addMessage(msg.sender, msg.text);
        });
    }
}

function sendToServer(userMessage) {
    // Tilføj bruger-besked til conversation
    conversation.push({ sender: "You", text: userMessage });
    saveChatHistory();

    // Vis i UI
    addMessage("You", userMessage);
    chatInput.value = '';

    // System prompt (valgfrit at sende her)
    const systemPrompt = {
        role: "system",
        content: "You are a friendly and knowledgeable AI Fitness Coach on an English-language health and fitness website."
    };

    // Kun send de sidste 10 beskeder
    const recentConversation = conversation.slice(-10);

    // Konverter til OpenAI format
    const chatMessages = recentConversation.map(msg => {
        if (msg.sender === "You") {
            return { role: "user", content: msg.text };
        } else {
            return { role: "assistant", content: msg.text };
        }
    });

    // Saml payload
    const payload = {
        messages: [systemPrompt, ...chatMessages]
    };

    // Kald /api/fitness_coach
    axios.post('/api/fitness_coach', payload)
        .then(response => {
            const reply = response.data.reply;
            conversation.push({ sender: "Coach", text: reply });
            saveChatHistory();
            addMessage("Coach", reply);
        })
        .catch(error => {
            console.error('Error:', error);
            const errorMsg = 'Sorry, something went wrong.';
            conversation.push({ sender: "Coach", text: errorMsg });
            saveChatHistory();
            addMessage("Coach", errorMsg);
        });
}

// Tilføj event listeners ved DOMContentLoaded
document.addEventListener('DOMContentLoaded', () => {
    // Hvis elementerne ikke findes, er chat-widgeten ikke på denne side
    if (!chatToggle || !chatWidget) return;

    loadChatHistory();

    chatToggle.addEventListener('click', () => {
        chatWidget.style.display = 'flex';
        chatToggle.classList.add('hide');
        if (conversation.length === 0) {
            const welcomeText = "Welcome! I am your AI Fitness Coach. Ask me anything about training and nutrition.";
            conversation.push({ sender: "Coach", text: welcomeText });
            saveChatHistory();
            addMessage("Coach", welcomeText);
        }
    });

    chatClose.addEventListener('click', () => {
        chatWidget.style.display = 'none';
        chatToggle.classList.remove('hide');
    });

    chatSend.addEventListener('click', () => {
        const message = chatInput.value.trim();
        if (!message) return;
        sendToServer(message);
    });

    chatInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            chatSend.click();
        }
    });
});
