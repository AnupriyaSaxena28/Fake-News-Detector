import React from 'react'
import Chatbot from './components/Chatbot'

export default function App(){
  return (
    <div className="app-root">
      <header className="header">
        <h1>AI Fake News Detector</h1>
        <p>Chat with the bot to verify news text or paste a URL</p>
      </header>
      <main>
        <Chatbot />
      </main>
    </div>
  )
}
