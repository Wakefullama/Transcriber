import whisper

# Load the base Whisper model
model = whisper.load_model("base")

# Transcribe an audio file (e.g., "audio.mp3")
result = model.transcribe("audio.mp3")

# Print the transcribed text
print(result["text"])
