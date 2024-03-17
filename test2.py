import pyaudio
import numpy as np
from faster_whisper import WhisperModel

# Definisci la dimensione del modello
model_size = "large-v3"

# Crea un'istanza del modello Whisper
model = WhisperModel(model_size, device="cuda", compute_type="float16")

# Configura PyAudio per catturare l'audio dal microfono
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Listening...")

try:
    while True:
        data = stream.read(CHUNK)
        audio = np.frombuffer(data, dtype=np.int16)

        # Trascrivi l'audio in tempo reale
        segments, _ = model.transcribe(audio, sample_rate=RATE)
        
        # Stampa i segmenti trascritti con i relativi tempi di inizio e fine
        for segment in segments:
            print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

except KeyboardInterrupt:
    print("Stopping...")
finally:
    stream.stop_stream()
    stream.close()
    p.terminate()
