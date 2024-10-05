import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './styles/index/index.css'
import { BrowserRouter } from 'react-router-dom';

// Монтируем приложение в корневой элемент с ID 'root'
ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);