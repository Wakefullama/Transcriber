from transformers import pipeline

def generate_formal_text(transcribed_text):
    # Carica il modello T5 per la generazione di testo
    ollie = pipeline("text2text-generation", model="T5ForConditionalGeneration", tokenizer="T5Tokenizer", device=0)  # Assicurati di selezionare il giusto dispositivo GPU se disponibile
    # Genera il testo formale in italiano
    formal_text = ollie(transcribed_text, max_length=50, num_return_sequences=1)[0]['generated_text']
    return formal_text
