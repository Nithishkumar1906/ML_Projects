# Machine Learning Journey

My hands-on ML/AI learning journey — experiments, implementations, and mini-projects built while learning classical ML, deep learning, and generative AI (LangChain, LangGraph, RAG, and LLM-powered apps).

## Overview

This repository contains notebooks and small applications built while learning machine learning and applied generative AI. Content is organized chronologically by learning topic — starting with classical NLP foundations and ending with applied GenAI practicals — plus a separate `projects/` folder for full Flask apps built along the way. Each notebook focuses on a specific concept or technique; each app project applies several of them together end-to-end.

## Learning Roadmap

| # | Topic | Notebooks | Key Concepts |
| - | ----- | --------- | ------------ |
| 01 | [NLP Foundations](./01-nlp-foundations/) | 7 | Text preprocessing, POS/NER tagging, lexicon sentiment analysis, bag-of-words classification, BERT/Transformer pipelines |
| 02 | [LangChain & LangGraph](./02-langchain-langgraph/) | 12 | LCEL, Runnables, output parsers, document loading, embeddings, Pinecone, short/long-term memory chatbots |
| 03 | [Deep Learning & Speech](./03-deep-learning-and-speech/) | 7 | CNNs, transfer learning, LSTM/GRU text generation, speech-to-text, text-to-speech |
| 04 | [RAG Pipelines & Evaluation](./04-rag-pipelines/) | 4 | RAG over PDFs, FAISS vs. Pinecone, local LLM serving (Ollama), RAGAS/BLEU/ROUGE evaluation |
| 05 | [Gradio & LLM Apps](./05-gradio-llm-apps/) | 5 | Streaming chatbots, tool calling, multi-agent dialogue, web scraping, brochure generation |
| 06 | [Applied GenAI & NLP](./06-applied-genai-nlp/) | 7 | Multimodal assistants, quantized local LLMs, code translation, classical ML vs. RNN vs. BERT sentiment analysis |

## 📂 Repository Structure

```text
ML_Projects/
│
├── 01-nlp-foundations/
├── 02-langchain-langgraph/
├── 03-deep-learning-and-speech/
├── 04-rag-pipelines/
├── 05-gradio-llm-apps/
├── 06-applied-genai-nlp/
│
├── projects/
│   ├── cancer-prediction-app/     # Flask app + training notebook
│   ├── chat-ai-assistant/         # Flask app: chat, PDF RAG, essay grading
│   └── resume-analyst-bot/        # Flask app: resume RAG summarizer/Q&A
│
├── .gitignore
└── README.md
```

Each topic folder has its own `README.md` with a per-notebook breakdown.

## Project Showcase

### [Breast Cancer Prediction App](./projects/cancer-prediction-app/)
- **Type:** Classification (deployed as a web app)
- **Objective:** Predict malignant vs. benign diagnosis from tumor measurements
- **Dataset:** [`Breast_cancer_data.csv`](./projects/cancer-prediction-app/Breast_cancer_data.csv) (569 records)
- **Model:** Random Forest (`n_estimators=500`)
- **Evaluation:** 92% test accuracy
- **Key Learning:** Serving a scikit-learn model through a Flask inference endpoint

### [Chat AI Assistant](./projects/chat-ai-assistant/)
- **Type:** LLM application (RAG + generation)
- **Objective:** General chat, PDF-based Q&A, and rubric-based essay grading in one app
- **Techniques:** PDF ingestion, chunking, local embeddings, FAISS similarity search, prompt construction
- **Models:** Gemini 1.5 Flash (generation), `sentence-transformers/all-MiniLM-L6-v2` (embeddings)
- **Key Learning:** Hand-rolling a RAG pipeline without a prebuilt LangChain chain

### [Resume Analyst Bot](./projects/resume-analyst-bot/)
- **Type:** LLM application (RAG)
- **Objective:** Summarize an uploaded resume and answer free-form questions about it
- **Techniques:** PDF extraction, chunking, FAISS index persistence, retrieval-augmented prompting
- **Models:** Gemini 1.5 Flash (generation), HuggingFace embeddings
- **Key Learning:** Persisting and reloading a vector store across requests

### [Sentiment Analysis: Classical vs. RNN vs. BERT](./06-applied-genai-nlp/sentiment-analysis-classical-vs-deep-vs-bert.ipynb)
- **Type:** Classification (model comparison)
- **Objective:** Compare five approaches to tweet sentiment classification on the same dataset
- **Dataset:** Sentiment140 (~1M+ tweets)
- **Models:** Logistic Regression, Linear SVM, SimpleRNN, LSTM, GRU, DistilBERT
- **Evaluation:** Accuracy, F1 — GRU and LSTM (84–86%) outperformed fine-tuned DistilBERT (75%) in this setup
- **Key Learning:** Model sophistication alone doesn't win — fine-tuning sample size and epoch budget matter

## Technology Stack

**Languages & Core:** Python, Jupyter Notebook

**Classical ML:** scikit-learn, pandas, NumPy, Matplotlib, Seaborn

**Deep Learning:** TensorFlow/Keras, PyTorch, HuggingFace Transformers

**NLP:** spaCy, NLTK, VADER, TextBlob

**Generative AI / LLM Tooling:** LangChain, LangGraph, Google Gemini API, Groq, Ollama, HuggingFace Diffusers

**Retrieval / Vector Search:** FAISS, Pinecone, sentence-transformers

**Speech:** OpenAI Whisper, SpeechRecognition, gTTS, librosa

**Apps & Deployment:** Flask, Gradio

## Learning Progression

```text
NLP Foundations (classical + transformer-based)
        ↓
LangChain & LangGraph fundamentals
        ↓
Deep Learning & Speech (CNNs, RNNs, STT/TTS)
        ↓
RAG Pipelines & Evaluation
        ↓
Gradio & LLM Apps (chatbots, tool calling, streaming)
        ↓
Applied GenAI & NLP (multimodal, quantized LLMs, model comparisons)
        ↓
Applied Projects (deployed Flask apps)
```

## Known Issues & Housekeeping

A few pre-existing issues were found and either fixed or flagged while reorganizing this repository — see each project's README for details:

- **Exposed API keys:** several notebooks and the two Gemini-based apps had live API keys hardcoded in source. The two app projects have been switched to load keys from a `.env` file (not committed); the affected notebooks are flagged in their topic README but left untouched. **All exposed keys should be rotated**, since they're already present in this repo's Git history.
- **`chat-ai-assistant/app.py` had an unresolved Git merge conflict** that made it non-functional (a syntax error). This has been resolved by keeping the intended Gemini/RAG app and discarding the unrelated, conflicting half.
- Two `requirements.txt` files were saved as UTF-16 (unreadable by `pip`) and have been re-saved as UTF-8; one was empty and has been filled in based on actual imports.
- Duplicate, Flask-unused copies of HTML templates (root-level copies of files that also existed under `templates/`) have been removed from both `cancer-prediction-app` and `chat-ai-assistant`.
- `resume-analyst-bot/uploads/` contains the developer's own resume files (real name, real history) and is not sanitized here — recommend deciding whether to purge them from Git history before treating this repo as public.

## Setup

Each notebook/app pins its own dependencies. From the relevant folder:

```bash
pip install -r requirements.txt
```

Several notebooks reference external datasets (Kaggle/public CSVs, personal audio recordings) that aren't committed to this repo — see the relevant topic README for which ones.
