# PDF Question Answering System

This project is a simple Python application that allows users to extract text from PDF documents and answer questions based on the content of those documents using TF-IDF and cosine similarity.

## Features

- Extracts text from multiple PDF files in a specified folder.
- Allows users to ask questions related to the extracted text.
- Uses TF-IDF vectorization and cosine similarity to find relevant sentences that answer the user's questions.

## Requirements

Make sure you have the following packages installed:

- `pdfplumber`
- `scikit-learn`
- `numpy`
- `re` (included in Python standard library)

You can install the required packages using pip:

```bash
pip install pdfplumber scikit-learn
```

## Usage

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the application:**

   ```bash
   python your_script.py
   ```

3. **Input the folder path:**

   When prompted, enter the path to the folder containing the PDF files you want to process.

4. **Ask questions:**

   You can now ask questions related to the content of the PDFs. Type your question and press Enter. Type `exit` to quit the application.

## Code Explanation

- **extract_text_from_pdf(pdf_path)**: Extracts text from a single PDF file.
- **extract_texts_from_folder(folder_path)**: Loads all PDF files from the specified folder and extracts their text.
- **vectorize_text(documents)**: Converts the extracted texts into TF-IDF vectors.
- **split_into_sentences(text)**: Splits a given text into sentences.
- **answer_question(question, documents, vectorizer)**: Takes a question and finds relevant sentences from the documents using cosine similarity.
- **main()**: The main function that coordinates the flow of the application.

## Example

```bash
Enter the path to the folder containing PDFs: /path/to/pdf/folder
Ask a question (or type 'exit' to quit): What is the main topic of the document?
Answer: The main topic is...
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [pdfplumber](https://github.com/jsvine/pdfplumber) for PDF text extraction.
- [Scikit-learn](https://scikit-learn.org/stable/) for machine learning utilities.
