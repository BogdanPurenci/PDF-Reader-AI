import os
import pdfplumber
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"  
    return text

def extract_texts_from_folder(folder_path):
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            text = extract_text_from_pdf(file_path)
            documents.append(text)
            print(f"Loaded: {filename}")
    return documents

def vectorize_text(documents):
    vectorizer = TfidfVectorizer()
    doc_vectors = vectorizer.fit_transform(documents)
    return vectorizer, doc_vectors

def split_into_sentences(text):
    sentences = re.split(r'(?<=[.!?]) +', text)
    return [sentence.strip() for sentence in sentences if sentence.strip()]

def answer_question(question, documents, vectorizer):
    question_vector = vectorizer.transform([question])
    
    relevant_sentences = []
    
    for doc in documents:
        sentences = split_into_sentences(doc)
        for sentence in sentences:
            sentence_vector = vectorizer.transform([sentence])
            similarity = cosine_similarity(question_vector, sentence_vector)

            # If similarity is above a threshold, consider it relevant
            if similarity[0][0] > 0.1:  # Adjust threshold as necessary
                relevant_sentences.append(sentence)

    return "\n".join(relevant_sentences) if relevant_sentences else "Nu am găsit informații relevante."

def main():
    folder_path = input("Enter the path to the folder containing PDFs: ")

    documents = extract_texts_from_folder(folder_path)
    
    if not documents:
        print("No PDFs found in the folder.")
        return

    # Vectorize the document texts
    vectorizer, _ = vectorize_text(documents)
    
    # Ask questions in a loop
    while True:
        question = input("\nAsk a question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Get the answer based on the question
        answer = answer_question(question, documents, vectorizer)
        print("\nAnswer:", answer)

# Run the main function
if __name__ == "__main__":
    main()
