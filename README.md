# Question-Answering-System

## Overview
This project is a command-line tool that allows users to ask natural language questions about a PDF document. The tool extracts text from the PDF, identifies relevant context, and generates detailed answers with citations to specific parts of the document.

---

## How to Run the Project

### 1. Clone the Repository
```
git clone https://github.com/Arittra-Bag/Question-Answering-System.git
cd Question-Answering-System
```
### 2. Install Dependencies
```
pip install -r requirements.txt
```
### 3. Set Up API Key
Create a ```.env``` file in the project directory:
```
OPENAI_API_KEY=your-api-key
```
### 4. Run the System
```
python src/question_answering.py <path-to-pdf> "<your-question>"
```
Example Command:
```
python src/question_answering.py ./tests/test_sample_1.pdf "What are the stylistic features of GPT's generated speeches?"
```
## Project Architecture

### 1. Text Extraction
**Module:** `pdf_reader.py`  
**Functionality:**  
- Uses the `PyPDF2` library to extract text from the provided PDF file.  
- Processes the PDF by iterating over each page and combining the text into a single string.  
- Handles exceptions gracefully if the file cannot be read.  

---

### 2. Answer Generation
**Module:** `openai_handler.py`  
**Functionality:**  
- Communicates with OpenAI's GPT-4o-mini model using the `openai.ChatCompletion.create` API.  
- Provides the entire document text and the user’s question as input.  
- Includes a system message prompting the model to:  
  - Answer the question based on the document.  
  - Include source information such as page numbers and headings in the response.  
- Handles API errors gracefully, ensuring robustness.  

---

### 3. Command-Line Interface
**Module:** `question_answering.py`  
**Functionality:**  
- Accepts two inputs from the user via the command line:  
  1. The path to the PDF file.  
  2. A natural language question about the document.  
- Calls `extract_text_from_pdf` to process the PDF and retrieve its text.  
- Sends the extracted text and the question to `get_answer_from_openai` for generating an answer.  
- Displays the generated answer in the console.  

---

## Design Pitfalls

1. **Dependency on OpenAI API**:
   - The system relies heavily on the OpenAI API, requiring an active internet connection and incurring usage costs.

2. **Token Limitations**:
   - OpenAI models have token limits, which may lead to truncated context or incomplete answers for large documents.

3. **Context Selection Accuracy**:
   - The system uses basic full-text extraction, which may not always select the most relevant context for complex queries.

4. **Citation Limitations**:
   - The accuracy of citations depends on the structure and readability of the PDF document.

---

## Safeguards for a Commercial Product

1. **Rate Limiting**:
   - Implement API rate limiting to control costs and ensure consistent performance under heavy usage.

2. **Data Privacy**:
   - Encrypt sensitive document content to ensure compliance with data protection regulations like GDPR.

3. **Improved Context Selection**:
   - Use embeddings-based models (e.g., OpenAI's `text-embedding-ada-002`) for better and more accurate context retrieval.

4. **Error Handling**:
   - Introduce robust error handling for invalid input, unreadable PDFs, or API connectivity issues.

5. **User Authentication**:
   - Add authentication to ensure only authorized users can interact with the system.

6. **Scalability**:
   - Optimize the backend for handling large files and concurrent users by implementing a chunking mechanism or serverless architecture.

---

## Future Improvements

1. **Support for Large Documents**:
   - Implement chunking to divide large PDFs into smaller sections for processing without hitting token limits.

2. **Integration with OCR**:
   - Add Optical Character Recognition (OCR) support using tools like Tesseract to process scanned or image-based PDFs.

3. **Enhanced User Interface**:
   - Develop a web-based UI or REST API for better usability and accessibility.

4. **Advanced Context Retrieval**:
   - Incorporate semantic search using vector embeddings for improved context selection.

5. **Real-Time Interaction**:
   - Enable real-time question-answering for live documents or evolving datasets.

---

## Contact

For any questions or issues, feel free to reach out:

Email: [arittrabag@gmail.com](mailto:arittrabag@gmail.com)  
GitHub: [https://github.com/Arittra-Bag](https://github.com/Arittra-Bag)  




