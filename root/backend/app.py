from flask import Flask, request, jsonify
from audio_processing import transcribe_audio
from ollie_model import generate_formal_text
from pdf_generator import generate_pdf

app = Flask(__name__)

@app.route('/transcribe', methods=['POST'])
def transcribe():
    audio_file = request.files['audio']
    if audio_file:
        transcribed_text = transcribe_audio(audio_file)
        formal_text = generate_formal_text(transcribed_text)
        pdf_bytes = generate_pdf(formal_text)
        return jsonify({'transcribed_text': transcribed_text, 'formal_text': formal_text, 'pdf_bytes': pdf_bytes})
    else:
        return jsonify({'error': 'No audio file provided'})

if __name__ == '__main__':
    app.run(debug=True)
