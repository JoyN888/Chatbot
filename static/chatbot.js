// Array to store conversation history
const conversationHistory = [];

// Handle the form submission and user input
document.getElementById('chatForm').addEventListener('submit', function (e) {
    e.preventDefault();

    // Get the user's message
    let userInput = document.getElementById('userInput').value.trim();

    if (userInput) {
        // Add user message to history
        addToHistory(userInput, 'User');

        // Display user message in the chat box
        appendMessage(userInput, 'userMsg');
        
        // Clear the input field
        document.getElementById('userInput').value = '';

        // Show typing indicator
        showTypingIndicator();

        // Simulate delay for bot response
        setTimeout(() => {
            // Get bot response
            let botResponse = getBotResponse(userInput);

            // Add bot response to history
            addToHistory(botResponse, 'Bot');

            // Hide typing indicator and display bot message
            hideTypingIndicator();
            appendMessage(botResponse, 'botMsg');
        }, 1000); // Simulate 1 second delay
    }
});

// Append messages to the chat box
function appendMessage(message, className) {
    const chatBox = document.getElementById('chatBox');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add(className);
    messageDiv.textContent = message;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to the bottom
}

// Add messages to conversation history
function addToHistory(message, sender) {
    const timestamp = new Date().toLocaleString(); // Get current timestamp
    conversationHistory.push({ sender, message, timestamp });

    // Optionally, log history to the console
    console.log("Conversation History:", conversationHistory);
}

// Show typing indicator
function showTypingIndicator() {
    const chatBox = document.getElementById('chatBox');
    const typingIndicator = document.createElement('div');
    typingIndicator.classList.add('typingIndicator');
    typingIndicator.setAttribute('id', 'typingIndicator');
    typingIndicator.textContent = 'Bot is typing...';
    chatBox.appendChild(typingIndicator);
    chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to show typing indicator
}

// Hide typing indicator
function hideTypingIndicator() {
    const typingIndicator = document.getElementById('typingIndicator');
    if (typingIndicator) {
        typingIndicator.remove();
    }
}

// Simple function to simulate bot responses
function getBotResponse(userMessage) {
    const responseMap = {
        "hi": "Hello! How can I assist you with your food-related queries today?",
        "hello": "Hi foodie-buddy! What can I get for you?",
        "hey": "Hey there! how can i help you with your food-related quires?",
        "special offers": "Currently, we have discounts on family meals and free delivery for orders over $50.",
        "working hours": "We're open daily from 9 AM to 11 PM.",
        "today special": "You made a good choice by visiting us, Today we have special menu which is Indian Food items they consist of Chicken Briyani, Nan Roti, Chicken curry, matar panner and etc",
        "great":"Any more quitions?",
        "no":"cool, let me know if you need any kind of help",
        "contact": "You can contact us at support@fastfoodchat.com or call us at 986542781.",
        "recommend": "I recommend trying our bestsellers: Margherita Pizza and Chocolate Lava Cake!",
        "menu": "We offer a variety of items, including cakes, fried rice, burgers, and more.",
        "delivery time": "Our average delivery time is 30 minutes.",
        "payment method": "We accept credit cards, debit cards, and online payment options.",
        "thanks": "You're welcome! Have a great day!",
        "bye": "Goodbye! Have a great day!"
    };

    userMessage = userMessage.toLowerCase();
    return responseMap[userMessage] || "Sorry, I didn't quite understand that. Could you please rephrase?";
}
