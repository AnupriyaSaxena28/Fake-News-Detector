import axios from 'axios'

const API_BASE = '/api'

export async function predictText(text){
  const res = await axios.post(`${API_BASE}/predict`, { text })
  return res.data
}

export async function predictURL(url){
  const res = await axios.post(`${API_BASE}/predict`, { url })
  return res.data
}
