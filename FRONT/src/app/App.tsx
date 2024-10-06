import './styles/App/App.css'
import BackGround from './assets/videos/bg.mp4'
import Header from '../widgets/header/ui/index'
import { Routes, Route} from 'react-router-dom';
import Main from '../pages/main/ui/index.tsx'
import React from 'react';

const App: React.FC = () => {

  return (
    <div className='wrapper'>
      <header className='Header'> <Header></Header> </header>
      <div className="video-container">
        <video autoPlay loop muted className="background-video">
          <source src={BackGround} type="video/mp4" />
          Your browser does not support the video tag.
        </video>
    </div>
    <main className="main">
        <Routes>
          <Route path="/" element={<Main />} />
        </Routes>
    </main>
    </div>
  )
}

export default App