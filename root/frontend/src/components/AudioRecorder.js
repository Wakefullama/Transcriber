import React, { useState } from 'react';
import MediaRecorder from 'react-media-recorder';

const AudioRecorder = () => {
  const [audioBlob, setAudioBlob] = useState(null);

  const handleAudioStop = (blob) => {
    setAudioBlob(blob);
  };

  return (
    <div>
      <MediaRecorder
        onRecordingStop={handleAudioStop}
        render={({ status, startRecording, stopRecording }) => (
          <div>
            <p>Recording status: {status}</p>
            <button onClick={startRecording}>Start Recording</button>
            <button onClick={stopRecording}>Stop Recording</button>
          </div>
        )}
      />
      {audioBlob && (
        <audio controls>
          <source src={URL.createObjectURL(audioBlob)} type="audio/wav" />
          Your browser does not support the audio element.
        </audio>
      )}
    </div>
  );
};

export default AudioRecorder;
