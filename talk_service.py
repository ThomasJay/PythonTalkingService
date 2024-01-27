from flask import Flask, request, jsonify
import pyttsx4

app = Flask(__name__)

api_v1_prefix = "/api/v1/"


engine = pyttsx4.init()

voices = engine.getProperty("voices")  # getting details of current voice

# Select Female Voice
engine.setProperty("voice", voices[6].id)


def speak(sentence):
    engine.say(sentence)

    engine.runAndWait()


@app.route("/", methods=["GET"])
def get_home():
    return "Talking Service"


@app.route(api_v1_prefix + "/health", methods=["GET"])
def get_health():
    return jsonify({"status": "Healthy"}), 200, {"Content-Type": "application/json"}


@app.route(api_v1_prefix + "/say", methods=["POST"])
def say():
    data = request.json

    print(data)

    speak(data.get("sentence"))

    return jsonify({"status": "Spoken"}), 200, {"Content-Type": "application/json"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8087)  # Auto reload
