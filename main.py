from ingest import multiple_files
from preprocessing import clean_text,split_text

folder_path = "docs" #replace docs with path to folder holding all files!!
raw_text = multiple_files(folder_path)
print("docs added, length of raw text is: ", len(raw_text))

cleaned = clean_text(raw_text)
print("cleaned, length of cleaned text is: ", len(cleaned))

chunks = split_text(cleaned, max_words=500)
print(f"Text split into {len(chunks)} chunks.")

#preview of first chunck
print("\n--- Preview of first chunk ---\n")
print(chunks[0])