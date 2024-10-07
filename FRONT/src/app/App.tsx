import './styles/App/App.css'
import BackGround from './assets/videos/bg.mp4'
import Header from '../widgets/header/ui/index' 
import React from 'react';
import Loading from '../pages/Loading/Loading.tsx'

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
      <Loading></Loading>
    </main>
    </div>
  )
}

export default App