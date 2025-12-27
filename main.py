from ingest import multiple_files
from preprocessing import clean_text,split_text

def load_and_preprocess_data(folder_path="docs", max_words=500): #replace docs
    # loading cleaning and chunking all documents in a reusable function
    raw_text = multiple_files(folder_path)
    cleaned_text = clean_text(raw_text)
    chunks = split_text(cleaned_text, max_words=max_words)
    return chunks
if __name__ == "__main__":
    chunks = load_and_preprocess_data("docs")
    print(f"Loaded {len(chunks)} chunks")
    print("\n--- Preview of first chunk ---\n")
    print(chunks[0])

