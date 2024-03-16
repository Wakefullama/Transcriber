from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(text):
    pdf_buffer = canvas.Canvas("transcribed_text.pdf", pagesize=letter)
    pdf_buffer.drawString(100, 750, text)
    pdf_buffer.save()
    with open("transcribed_text.pdf", "rb") as file:
        pdf_bytes = file.read()
    return pdf_bytes
