
# Chatbot Code using Flask for Backend
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def chatbot_response(user_input):
    # Simple rule-based responses
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing fine. How can I assist you?",
        "bye": "Goodbye! Have a great day!"
    }
    user_input = user_input.lower()
    return responses.get(user_input, "I'm sorry, I didn't understand that. Can you rephrase?")


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    print("Received data", data)
    user_message = data.get("message", "")
    bot_reply = chatbot_response(user_message)
    return jsonify({"response": bot_reply})


if __name__ == "__main__":
    app.run(debug=True)
