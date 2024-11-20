import nltk
from nltk.chat.util import Chat, reflections

# Download necessary NLTK data files (only needed once)
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    [r"(hi|hello|hey)", ["Hello! How can I assist you with your food-related queries today?"]],
    [r"(.*)menu(.*)", ["Our menu includes cakes, fried rice, pizza, and more!"]],
    [r"(.*)delivery time(.*)", ["Our average delivery time is 30 minutes."]],
    [r"(.*)payment methods(.*)", ["We accept credit/debit cards, UPI, and cash on delivery."]],
    [r"(.*)special offers(.*)", ["Currently, we have discounts on family meals and free delivery for orders over $50."]],
    [r"(.*)working hours(.*)", ["We're open daily from 9 AM to 11 PM."]],
    [r"(.*)contact(.*)", ["You can contact us at support@fastfoodchat.com or call us at 123-456-7890."]],
    [r"(.*)recommend(.*)", ["I recommend trying our bestsellers: Margherita Pizza and Chocolate Lava Cake!"]],
    [r"quit", ["Goodbye! Have a great day!"]],
]


# Initialize chatbot with pairs and reflections
chatbot = Chat(pairs, reflections)

# Start the chatbot
print("Chatbot is ready! Type 'quit' to exit.")
chatbot.converse()
def custom_chat():
    print("Chatbot is ready! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye! Have a nice day.")
            break
        response = chatbot.respond(user_input)
        if response:
            print("Chatbot:", response)
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Could you please rephrase?")

custom_chat()
