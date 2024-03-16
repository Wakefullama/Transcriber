import React, { useState } from 'react';
import Dropzone from 'react-dropzone';

const AudioUploader = () => {
  const [audioFile, setAudioFile] = useState(null);

  const handleDrop = (acceptedFiles) => {
    setAudioFile(acceptedFiles[0]);
  };

  return (
    <div>
      <Dropzone onDrop={handleDrop} accept="audio/*">
        {({ getRootProps, getInputProps }) => (
          <div {...getRootProps()}>
            <input {...getInputProps()} />
            <p>Drag 'n' drop an audio file here, or click to select one</p>
          </div>
        )}
      </Dropzone>
      {audioFile && <p>Selected audio file: {audioFile.name}</p>}
    </div>
  );
};

export default AudioUploader;
