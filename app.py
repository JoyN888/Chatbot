import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet, stopwords
from nltk.stem import WordNetLemmatizer
from flask import Flask, render_template, request
from nltk.chat.util import Chat, reflections

# Initialize Flask app
app = Flask(__name__)

# Download required NLTK data
nltk.download("punkt")
nltk.download("wordnet")
nltk.download("stopwords")

# Initialize lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

# Updated Chatbot logic with NLP preprocessing
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

chatbot = Chat(pairs, reflections)


# NLP preprocessing functions
def preprocess_input(user_input):
    """Preprocess user input by tokenizing, removing stopwords, and lemmatizing."""
    tokens = word_tokenize(user_input.lower())
    processed = [lemmatizer.lemmatize(word) for word in tokens if word.isalpha() and word not in stop_words]
    return processed


def get_synonyms(word):
    """Fetch synonyms for a given word."""
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return synonyms


# Enhanced response logic
def get_bot_response(user_input):
    """Return chatbot's response based on enhanced logic."""
    processed_input = preprocess_input(user_input)

    if not processed_input:
        return "I couldn't understand that. Can you please clarify?"

    for pattern, responses in pairs:
        # Check for match in user input or synonyms
        for word in processed_input:
            if word in pattern or any(syn in pattern for syn in get_synonyms(word)):
                return responses[0]

    return "I'm sorry, I don't have an answer for that. Can you ask something else?"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/get", methods=["GET", "POST"])
def get_response():
    user_input = request.args.get("msg")  # Get user's message
    return get_bot_response(user_input)  # Return chatbot's enhanced response


if __name__ == "__main__":
    app.run(debug=True)
