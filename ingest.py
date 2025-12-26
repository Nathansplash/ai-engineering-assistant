# handels ingestion and preprocessing of techinical documents
import os
from PyPDF2 import PdfReader, PdfFileReader


def read_data(path):
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    if path.endswith('.pdf'):
        return read_pdf(path)
    with open(path, "r", encoding="utf-8") as file:
        data = file.read()
    return data
def read_pdf(path):
    #adding pdf support
    text = " "
    for page in PdfReader(path).pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text
def multiple_files(folder):
    # combining files
    combined = " "
    for file in os.listdir(folder):
        if file.endswith(".txt") or file.endswith(".pdf"):
            file_path = os.path.join(folder, file)
            combined += read_data(file_path) + "\n"
    return combined