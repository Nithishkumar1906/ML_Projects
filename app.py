GEM_API_KEY="AIzaSyAh0ctdkQt4d9xI4i3cg_wTViDeSo0iROo"

import os,re
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from flask import Flask, render_template, request, redirect
from PyPDF2 import PdfReader
import google.generativeai as genai
from langchain.text_splitter import CharacterTextSplitter


start_greeting = ["Hi","Hello"]
end_greeting = ["bye! see you again"]
way_greeting = ["Who are you?"]

Data_Dir = "__data__"
if not os.path.exists(Data_Dir):
    os.makedirs(Data_Dir)


app = Flask(__name__)

vectorstore = None
conversation_chain = None
chat_history = []
rubric_text = ""
genai.configure(api_key=GEM_API_KEY)
gemini_model = genai.GenerativeModel("models/gemini-1.5-flash")



def get_pdf_text(pdf_docs):
    """
    Extracts and combines text content from a list of PDF files.

    For each uploaded PDF:
    - Extracts text from all pages.
    - Saves the text into a `.txt` file in the DATA_DIR with the same name as the PDF.
    - Combines the text from all PDFs into a single string.

    Args:
        pdf_docs (list): List of uploaded PDF files (e.g., from a web form).

    Returns:
        str: Combined text content from all uploaded PDFs.
    """
    text = ""
    pdf_txt = ""
    for pdf in pdf_docs:
        filename = os.path.join(Data_Dir, pdf.filename)
        pdf_txt = ""
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
            pdf_txt += page.extract_text()

        with (open(filename, "w", encoding="utf-8")) as op_file:
            op_file.write(pdf_txt)

    return text


def get_text_chunks(text):
    """
    Splits the given text into smaller overlapping chunks for better processing.

    Uses a character-based splitter that breaks the text into chunks of up to 
    1000 characters, with an overlap of 200 characters between chunks. 
    This helps preserve context in use cases like embedding, summarization, or QA.

    Args:
        text (str): The input text to be split.

    Returns:
        list: A list of text chunks (strings) created from the original input text.
    """
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore



def get_conversation_chain(vectorstore):
    def conversation_chain(user_question):
        context_docs = vectorstore.similarity_search(user_question, k=3)
        context_text = "\n\n".join([doc.page_content for doc in context_docs])
        prompt = f"""Answer the question based on the following context:

Context:
{context_text}

Question:
{user_question}
"""

        response = gemini_model.generate_content(prompt)
        return response.text
    return conversation_chain


def _grade_essay(essay):
    full_prompt = f"""You are a Student bot. You are supposed to carefully grade the essay based on the following rubric and respond.

Rubric:
{rubric_text}

Essay:
{essay}
"""
    response = gemini_model.generate_content(full_prompt)
    data = response.text
    data = re.sub(r'\n', '<br>', data)
    return data


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/process', methods=['POST'])
def process_documents():
    global vectorstore, conversation_chain
    pdf_docs = request.files.getlist('pdf_docs')
    raw_text = get_pdf_text(pdf_docs)
    text_chunks = get_text_chunks(raw_text)
    vectorstore = get_vectorstore(text_chunks)
    conversation_chain = get_conversation_chain(vectorstore)
    return redirect('/chat')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    global vectorstore, conversation_chain, chat_history
    msgs = []
    
    if request.method == 'POST':
        user_question = request.form['user_question']
        
        answer = conversation_chain(user_question)
        chat_history.append(("User", user_question))
        chat_history.append(("Bot", answer))

        
    return render_template('new_chat.html', chat_history=chat_history)

@app.route('/pdf_chat', methods=['GET', 'POST'])
def pdf_chat():
    return render_template('pdf_chat.html')

@app.route('/essay_grading', methods=['GET', 'POST'])
def essay_grading():
    result = None
    if request.method == 'POST':
        if request.form.get('essay_rubric', False):
            global rubric_text
            rubric_text = request.form.get('essay_rubric')

            return render_template('new_essay_grad.html')
        
        if len(request.files['file'].filename) > 0:
            pdf_file = request.files['file']
            text = extract_text_from_pdf(pdf_file)
            result = _grade_essay(text)
        else:
            text = request.form.get('essay_text')
            result = _grade_essay(text)
    
    return render_template('new_essay_grad.html', result=result, input_text=text)

    
@app.route('/essay_rubric', methods=['GET', 'POST'])
def essay_rubric():
    return render_template('new_essay.html')

def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page_num].extract_text()
    return text

if __name__ == '__main__':
    print("✅ Flask app is starting...")
    app.run(debug=True)
