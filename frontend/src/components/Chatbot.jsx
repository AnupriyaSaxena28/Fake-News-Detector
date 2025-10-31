import React, {useState, useRef, useEffect} from 'react'
import { predictText, predictURL } from '../api'

export default function Chatbot(){
  const [messages, setMessages] = useState([
    {from: 'bot', text: 'Hello! Paste text or a news URL and I will check if it is real or fake.'}
  ])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const messagesRef = useRef(null)

  useEffect(()=>{ messagesRef.current?.scrollTo({ top: messagesRef.current.scrollHeight, behavior: 'smooth' }) }, [messages])

  async function send(){
    if(!input.trim()) return
    const userMsg = {from: 'user', text: input}
    setMessages(m => [...m, userMsg])
    setInput('')
    setLoading(true)
    try{
      let result
      if(input.startsWith('http')){
        result = await predictURL(input)
      } else {
        result = await predictText(input)
      }
      const botText = `Prediction: ${result.prediction}${result.confidence ? ` (confidence: ${Math.round(result.confidence*100)}%)` : ''}`
      setMessages(m => [...m, {from: 'bot', text: botText}])
    } catch(err){
      setMessages(m => [...m, {from: 'bot', text: 'Error: Could not reach the API.'}])
      console.error(err)
    } finally{
      setLoading(false)
    }
  }

  function onKey(e){ if(e.key === 'Enter') send() }

  return (
    <div className="chatbot-container">
      <div className="messages" ref={messagesRef}>
        {messages.map((m, i) => (
          <div key={i} className={`message ${m.from}`}>
            <div className="bubble">{m.text}</div>
          </div>
        ))}
      </div>
      <div className="composer">
        <input
          placeholder="Paste text or a news URL..."
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={onKey}
        />
        <button onClick={send} disabled={loading}>{loading ? 'Checking...' : 'Send'}</button>
      </div>
    </div>
  )
}
