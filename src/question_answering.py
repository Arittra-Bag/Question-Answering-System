import argparse
from pdf_reader import extract_text_from_pdf
from openai_handler import get_answer_from_openai

def main():
    parser = argparse.ArgumentParser(description='Legal Contract QA System')
    parser.add_argument('pdf_path', type=str, help='Path to the PDF document')
    parser.add_argument('question', type=str, help='Question about the document')
    args = parser.parse_args()

    try:
        document_text = extract_text_from_pdf(args.pdf_path)
        answer = get_answer_from_openai(document_text, args.question)
        print(f"Answer: {answer}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
