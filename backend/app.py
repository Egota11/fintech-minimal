import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "status": "online",
        "message": "FinTech AI API çalışıyor - Minimal Mode",
        "version": "0.1.0"
    })

@app.route('/api/advice/public-ai-response', methods=['POST'])
def get_public_ai_response():
    return jsonify({
        'response': "FinTech AI şu anda bakım modundadır. AI özellikleri yakında tekrar aktif olacaktır."
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', debug=False, port=port)
