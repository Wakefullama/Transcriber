# Usa un'immagine di Python ufficiale come base
FROM python:3.11-slim

# Imposta il lavoro directory nell'applicazione
WORKDIR /app

# Copia il file con i requisiti nella directory dell'applicazione
COPY requirements.txt requirements.txt

# Installa le dipendenze Python
RUN pip install --no-cache-dir -r requirements.txt
 
# Copia tutti i file dell'applicazione nella directory dell'applicazione
COPY . .

# Espone la porta su cui l'applicazione FastAPI è in ascolto
EXPOSE 3000

# Comando per eseguire l'applicazione utilizzando uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9090"]
