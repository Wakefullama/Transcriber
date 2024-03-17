import pyaudio
import wave
import os
import tempfile
import yaml
import ctranslate2

def transcribe_audio(stream, model):
    # Configura la finestra temporanea per la registrazione dell'audio
    temp_filename = tempfile.mktemp(suffix=".wav")
    frames = []

    # Registra l'audio in tempo reale e scrive i frame nel file temporaneo
    print("Inizia la registrazione...")
    for _ in range(int(SAMPLE_RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
        audio_file.writeframes(data)

        # Trascrivi l'audio mentre viene registrato
        segments, _ = model.transcribe(audio_file.name)
        transcription = "\n".join([segment.text for segment in segments])
        print(f"Trascrizione in tempo reale: {transcription}")

    print("Fine registrazione.")
    stream.stop_stream()
    stream.close()
    audio_file.close()
    os.remove(temp_filename)

# Parametri per la registrazione audio
FORMAT = pyaudio.paInt16
CHANNELS = 1
SAMPLE_RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5  # Durata della registrazione in secondi

# Carica le impostazioni del modello da un file di configurazione YAML
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)
    model_name = config.get("model_name", "base.en")
    device_type = config.get("device_type", "cpu")
    quantization_type = config.get("quantization_type", "int8")

# Inizializza il modello di riconoscimento vocale
model_str = f"ctranslate2-4you/whisper-{model_name}-ct2-{quantization_type}"
model = ctranslate2.Translator(model_str, device=device_type)

# Inizializza PyAudio per la registrazione audio
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=SAMPLE_RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Esegui la trascrizione audio in tempo reale
try:
    transcribe_audio(stream, model)
finally:
    p.terminate()
