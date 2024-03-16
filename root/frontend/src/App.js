import React, { useState } from 'react';
import './styles.css';
import AudioRecorder from './components/AudioRecorder';
import AudioUploader from './components/AudioUploader';
import TextDisplay from './components/TextDisplay';
import PdfGenerator from './components/PdfGenerator';

const App = () => {
  const [transcribedText, setTranscribedText] = useState('');

  const handleTranscription = (text) => {
    setTranscribedText(text);
  };

  return (
    <div className="container">
      <h1>Audio to Formal Text</h1>
      <div className="row">
        <div className="col">
          <AudioRecorder onTranscription={handleTranscription} />
          <AudioUploader onTranscription={handleTranscription} />
        </div>
        <div className="col">
          <TextDisplay text={transcribedText} />
          <PdfGenerator text={transcribedText} />
        </div>
      </div>
    </div>
  );
};

export default App;
