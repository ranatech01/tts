import asyncio
import edge_tts
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Taaki aapki website isse connect kar sake


@app.route('/generate-tts', methods=['POST'])
def generate_tts():
    data = request.json
    text = data.get('text')
    voice = data.get('voice', 'en-US-JennyNeural')  # Default voice
    rate = data.get('rate', '+0%')  # Default speed

    if not text:
        return jsonify({"error": "No text provided"}), 400

    output_file = "output.mp3"

    # Edge TTS logic
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    asyncio.run(communicate.save(output_file))

    return send_file(output_file, mimetype="audio/mpeg")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)