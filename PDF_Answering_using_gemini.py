import PyPDF2
import os
import google.generativeai as genai
os.environ['GOOGLE_API_KEY'] = 'YOUR_API_KEY'
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text


pdf_file_name = input('Enter pdf name : ')
pdf_text = extract_text_from_pdf(pdf_file_name)
question = input("Enter your question : ")
model = genai.GenerativeModel('gemini-pro')
prompt = f"Context: {pdf_text}\n\nQuestion: {question}"

response = model.generate_content(prompt)
print('Answer : ')
print(response.text)

