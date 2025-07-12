from flask import Flask, request, jsonify
import whisper
import os

app = Flask(__name__)

# Load whisper model (use base, small, or medium depending on your system)
model = whisper.load_model("base")

@app.route('/upload', methods=['POST'])
def upload():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file uploaded'}), 400

    audio = request.files['audio']
    filename = audio.filename
    filepath = os.path.join("uploads", filename)
    os.makedirs("uploads", exist_ok=True)
    audio.save(filepath)

    # Transcribe using whisper
    result = model.transcribe(filepath)
    transcript = result['text']

    return jsonify({
        "transcript": transcript,
        "prescription": "Detected prescription from speech (simulate here)"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
