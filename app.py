from flask import Flask, render_template, request, jsonify
import ollama

app = Flask(__name__)

# Stores conversation history for memory
conversation_history = []

def chat(user_message):
    """Send a message to Llama and get a response."""
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant. Answer questions clearly and honestly."
            }
        ] + conversation_history
    )

    assistant_message = response["message"]["content"]

    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })

    return assistant_message


@app.route("/")
def index():
    """Serve the chat page."""
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat_endpoint():
    """Receive a message and return AI response."""
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    response = chat(user_message)
    return jsonify({"response": response})


@app.route("/clear", methods=["POST"])
def clear_history():
    """Clear the conversation history."""
    global conversation_history
    conversation_history = []
    return jsonify({"status": "cleared"})


if __name__ == "__main__":
    app.run(debug=True)