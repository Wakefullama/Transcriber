# Usa un'immagine base di Python
FROM python:3.9-slim

# Imposta la directory di lavoro nel container
WORKDIR /app

# Copia il file delle dipendenze Python
COPY requirements.txt .

# Installa le dipendenze Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia il codice sorgente nella directory di lavoro
COPY . .

# Avvia il backend Flask
CMD ["python", "app.py"]
