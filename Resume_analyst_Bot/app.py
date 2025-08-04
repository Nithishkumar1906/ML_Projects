from flask import Flask, request, render_template, redirect, url_for
import os
import re
from werkzeug.utils import secure_filename
import PyPDF2
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
import google.generativeai as genai

# ✅ Gemini API Key Configuration
genai.configure(api_key="AIzaSyAh0ctdkQt4d9xI4i3cg_wTViDeSo0iROo")
gemini_model = genai.GenerativeModel("models/gemini-1.5-flash")

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Text splitter for breaking resume into chunks
text_splitter = CharacterTextSplitter(
    separator='\n',
    chunk_size=2000,
    chunk_overlap=200,
    length_function=len,
)

# Embedding model to convert text into searchable vectors
embeddings = HuggingFaceEmbeddings()

def extract_text_from_pdf(pdf_path):
    """
    Extracts all text from the uploaded PDF file.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Combined text extracted from all pages of the PDF.
    """
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def generate_resume_summary(text):
    """
    Generates a professional resume summary using Gemini AI.

    Args:
        text (str): The full resume text.

    Returns:
        str: AI-generated structured summary of the resume.
    """
    prompt = f"""
Role: You are an AI Career Coach.

Task: Given the candidate's resume, provide a comprehensive summary that includes the following key aspects:
- Career Objective
- Skills and Expertise
- Professional Experience
- Educational Background
- Notable Achievements

Resume:
{text}
"""
    response = gemini_model.generate_content(prompt)
    return response.text

def perform_qa(query):
    """
    Answers a user question based on the resume content using Gemini AI.

    Args:
        query (str): The question asked by the user.

    Returns:
        str: AI-generated answer based on the resume context.
    """
    db = FAISS.load_local("vector_index", embeddings, allow_dangerous_deserialization=True)
    docs = db.similarity_search(query, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
Based on the following resume information, answer the question clearly.

Resume:
{context}

Question:
{query}
"""
    response = gemini_model.generate_content(prompt)
    return response.text

@app.route('/')
def index():
    """
    Home route to render the resume upload page.
    """
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handles PDF upload, text extraction, vector store creation,
    and triggers resume summary generation.

    Returns:
        Renders the summary result page.
    """
    if 'file' not in request.files:
        return redirect(url_for('index'))
    
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))
    
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        resume_text = extract_text_from_pdf(file_path)
        splitted_text = text_splitter.split_text(resume_text)
        vectorstore = FAISS.from_texts(splitted_text, embeddings)
        vectorstore.save_local("vector_index")

        resume_analysis = generate_resume_summary(resume_text)
        return render_template('results.html', resume_analysis=resume_analysis)

@app.route('/ask', methods=['GET', 'POST'])
def ask_query():
    """
    Route to ask a custom question based on the uploaded resume.

    Returns:
        GET: Renders the ask page.
        POST: Renders the QA result page.
    """
    if request.method == 'POST':
        query = request.form['query']
        result = perform_qa(query)
        return render_template('qa_results.html', query=query, result=result)
    return render_template('ask.html')

if __name__ == "__main__":
    app.run(debug=True)
