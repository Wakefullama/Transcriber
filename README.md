## Frontend (ReactJS con Bootstrap):
- index.html: File principale HTML che carica l'app React.
- App.js: Componente principale React che gestisce lo stato dell'applicazione e il rendering dell'interfaccia utente.
- AudioRecorder.js: Componente React per la registrazione audio in tempo reale.
- AudioUploader.js: Componente React per il caricamento dei file audio.
- TextDisplay.js: Componente React per visualizzare il testo trascritto.
- PdfGenerator.js: Componente React per generare e scaricare il documento PDF.
- styles.css: Foglio di stile per personalizzare l'aspetto dell'applicazione.
## Backend (Python con Flask):
- app.py: File principale che avvia il server Flask e gestisce le richieste HTTP.
- audio_processing.py: Modulo Python per l'elaborazione dei file audio, inclusa la trascrizione.
- ollie_model.py: Modulo Python per l'integrazione del modello OLLIE.
- pdf_generator.py: Modulo Python per la generazione del documento PDF.
- requirements.txt: File di testo che elenca tutte le dipendenze Python del progetto.
## Altri file:
- README.md: Documentazione del progetto, inclusi istruzioni per l'installazione e l'utilizzo.
- LICENSE: Licenza del software che specifica i diritti e le restrizioni per l'utilizzo del codice.

## STRUTTURA:
root/
│
├── frontend/
│   ├── public/
│   │   ├── index.html
│   │   └── favicon.ico
│   ├── src/
│   │   ├── components/
│   │   │   ├── AudioRecorder.js
│   │   │   ├── AudioUploader.js
│   │   │   ├── TextDisplay.js
│   │   │   └── PdfGenerator.js
│   │   ├── App.js
│   │   └── index.js
│   ├── styles.css
│   ├── Dockerfile
│   ├── package.json        # Aggiunto
│
├── backend/
│   ├── app.py
│   ├── audio_processing.py
│   ├── ollie_model.py
│   ├── pdf_generator.py
│   ├── requirements.txt
│   ├── Dockerfile
│
├── README.md
├── LICENSE
├── docker-compose.yml
└── .dockerignore



frontend/: Contiene tutti i file relativi al frontend dell'applicazione.
    public/: Contiene file pubblici come l'HTML principale e l'icona del sito.
        src/: Contiene il codice sorgente ReactJS dell'applicazione.
            components/: Contiene i componenti React riutilizzabili.
            App.js: Il componente principale che definisce la struttura dell'applicazione.
            index.js: File di avvio che rende l'applicazione React all'interno del documento HTML.
        styles.css: Il foglio di stile per personalizzare l'aspetto dell'applicazione.
backend/: Contiene tutti i file relativi al backend dell'applicazione.
    app.py: Il file principale che avvia il server Flask e gestisce le richieste HTTP.
    audio_processing.py: Modulo Python per l'elaborazione dei file audio.
    ollie_model.py: Modulo Python per l'integrazione del modello OLLIE.
    pdf_generator.py: Modulo Python per la generazione del documento PDF.
    requirements.txt: Elenco delle dipendenze Python del progetto.
README.md: Documentazione del progetto con istruzioni per l'installazione e l'utilizzo.

LICENSE: Licenza del software che specifica i diritti e le restrizioni per l'utilizzo del codice.