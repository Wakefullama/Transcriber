import React from 'react';

const TextDisplay = ({ text }) => {
  return (
    <div>
      <h2>Transcribed Text:</h2>
      <p>{text}</p>
    </div>
  );
};

export default TextDisplay;
