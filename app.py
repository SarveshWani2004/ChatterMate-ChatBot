from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def bot_response(msg):
    msg = msg.lower()
    if "hello" in msg or "hi" in msg:
        return "Hi there! How can I help you today?"
    elif "your name" in msg:
        return "I’m ChatterMate, your friendly chatbot!"
    elif "help" in msg:
        return "Sure! Ask me anything or say 'hi' to start."
    else:
        return "I'm not sure how to respond to that yet."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_bot_response():
    user_msg = request.args.get("msg")
    return jsonify(response=bot_response(user_msg))

if __name__ == "__main__":
    app.run(debug=True)
