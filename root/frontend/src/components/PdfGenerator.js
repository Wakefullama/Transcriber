import React from 'react';
import jsPDF from 'jspdf';

const PdfGenerator = ({ text }) => {
  const handleGeneratePdf = () => {
    // Crea un nuovo documento PDF
    const doc = new jsPDF();
    
    // Aggiungi il testo al documento
    doc.text(text, 10, 10);
    
    // Salva il documento come file PDF
    doc.save('transcribed_text.pdf');
  };

  return (
    <div>
      <button onClick={handleGeneratePdf}>Generate PDF</button>
    </div>
  );
};

export default PdfGenerator;
