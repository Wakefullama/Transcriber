# Usa un'immagine base di Node.js
FROM node:14-alpine

# Imposta la directory di lavoro nel container
WORKDIR /app

# Copia il package.json e package-lock.json nella directory di lavoro
COPY package.json ./

# Installa le dipendenze
RUN npm install

# Copia il codice sorgente nella directory di lavoro
COPY . .

# Avvia l'applicazione React
CMD ["npm", "start"]
