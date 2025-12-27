import os
import openai
from main import load_and_preprocess_data

#api key
openai_api_key = os.environ.get('OPENAI_API_KEY')

chunks = load_and_preprocess_data('docs')
print(f"Loaded {len(chunks)} chunks from documents.")

def get_relevant_chunks(question, chunks, top_k=3):
    #this function selects the top 3 chunks that contain words from the question
    question_words = set(question.lower().split())
    scored_chunks = []
    for chunk in chunks:
        chunk_words = set(chunk.lower().split())
        score = len(question_words & chunk_words)
        scored_chunks.append(score)
    scored_chunks.sort(reverse=True)
    return [c for _, c in scored_chunks[:top_k]]
def ask_question(question):
    relevent_chunks = get_relevant_chunks(question)
    context = "\n\n".join(relevent_chunks)
    prompt = f"Answer the question using ONLY the context below:\n\n{context}\n\nQuestion: {question}\nAnswer:"
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 300)
    return response.choices[0].text.strip()
if __name__ == "__main__":


