import requests
from bs4 import BeautifulSoup
import json

# Documentation URLs
urls = {
    "Segment": "https://segment.com/docs/",
    "mParticle": "https://docs.mparticle.com/",
    "Lytics": "https://docs.lytics.com/",
    "Zeotap": "https://docs.zeotap.com/home/en-us/"
}

def scrape_docs():
    docs = {}
    for platform, url in urls.items():
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = ' '.join([p.text for p in soup.find_all('p')])
        docs[platform] = text
    
    with open('docs.json', 'w') as f:
        json.dump(docs, f)

if __name__ == "__main__":
    scrape_docs()
