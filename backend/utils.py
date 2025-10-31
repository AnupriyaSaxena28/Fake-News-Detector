# utils.py — preprocessing helpers
import re
import nltk
from nltk.corpus import stopwords

try:
    stopwords.words('english')
except Exception:
    nltk.download('stopwords')

STOPWORDS = set(stopwords.words('english'))

def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return ''
    text = re.sub(r'http\S+', '', text)  # remove urls
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    tokens = text.lower().split()
    tokens = [t for t in tokens if t not in STOPWORDS and len(t) > 1]
    return ' '.join(tokens)

# optional: function to extract article text from URL (simple)
from bs4 import BeautifulSoup
import requests

def extract_text_from_url(url: str) -> str:
    try:
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')
        paragraphs = soup.find_all('p')
        return '\n'.join(p.get_text() for p in paragraphs)
    except Exception:
        return ''
