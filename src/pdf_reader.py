from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            text += page.extract_text()
    except Exception as e:
        raise Exception(f"Error reading PDF file: {e}")
    return text
