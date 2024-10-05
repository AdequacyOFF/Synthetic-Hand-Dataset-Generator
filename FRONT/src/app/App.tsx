import './styles/App/App.css'
import BackGround from './assets/videos/bg.mp4'
import Header from '../widgets/header/ui/index'
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Main from '../pages/main/ui/index.tsx'
import Loading from '../pages/downloadSite/ui/index.tsx'

function App() {

  return (
    <div className='wrapper'>
      <header className='Header'> <Header></Header> </header>
      <div className="video-container">
      <video autoPlay loop muted className="background-video">
        <source src={BackGround} type="video/mp4" />
        Your browser does not support the video tag.
      </video>
      <main className="main">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Loading />} />
          <Route path="/main" element={<Main />} />
        </Routes>
      </BrowserRouter>
      </main>
    </div>

    </div>
  )
}

export default App