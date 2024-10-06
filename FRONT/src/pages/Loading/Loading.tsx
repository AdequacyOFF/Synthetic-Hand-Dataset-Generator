// src/FullscreenVideo.tsx

import React, { useState } from 'react';
import loadingPage from '../../app/assets/videos/loadingPage.mp4'

const Loading: React.FC = () => {
  const [isVisible, setIsVisible] = useState(true);

  const handleVideoEnded = () => {
    setIsVisible(false);
  };

  return (
    <div>
      {isVisible && (
        <video
          src={loadingPage} 
          autoPlay
          muted
          onEnded={handleVideoEnded}
          style={{
            position: 'fixed',
            top: 0,
            left: 0,
            width: '100%',
            height: '100%',
            objectFit: 'cover',
            zIndex: '1000',
          }}
        />
      )}
    </div>
  );
};

export default Loading;