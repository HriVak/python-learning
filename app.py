from flask import Flask, request, jsonify
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")
app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json["message"]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": msg}]
    )

    reply = response.choices[0].message.content
    return jsonify({"reply": reply})

app.run()
