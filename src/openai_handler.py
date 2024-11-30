import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key not found. Please set it in the .env file.")

openai.api_key = OPENAI_API_KEY

def get_answer_from_openai(document_text, question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers questions based on a document. Please include the source information (page number and heading) in your response."},
                {"role": "user", "content": f"Document: {document_text}\n\nQuestion: {question}"}
            ]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        raise Exception(f"Error communicating with OpenAI API: {e}")
