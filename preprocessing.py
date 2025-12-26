import re

def clean_text(text):
    #cleaning text ( removing white spaces, and unwanted characters)
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r' +', ' ', text)
    text = text.strip()
    return text
def split_text(text, max_words=500):
    #splitting text into chunks of 500 words
    words = text.split()
    chunks = []
    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i+max_words])
        chunks.append(chunk)
    return chunks