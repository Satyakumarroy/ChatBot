import json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Load the scraped data
with open('docs.json', 'r') as f:
    docs = json.load(f)

# Stopwords for filtering
stop_words = set(stopwords.words('english'))

def search_docs(query):
    results = {}
    tokens = [word.lower() for word in word_tokenize(query) if word.isalnum() and word.lower() not in stop_words]
    
    for platform, content in docs.items():
        if any(token in content.lower() for token in tokens):
            results[platform] = content[:500]  # Return first 500 characters as a preview
    
    return results
