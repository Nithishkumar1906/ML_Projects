# Chat AI Assistant

## Overview

A multi-feature Flask app built on Google's Gemini API: general chat, PDF-based RAG chat, and essay grading against a rubric.

## Features

| Route | Method | Description |
| --- | --- | --- |
| `/` | GET | Landing page with links to each feature |
| `/process` | POST | Uploads one or more PDFs, extracts text (`PyPDF2`), chunks it (`CharacterTextSplitter`), embeds it (`sentence-transformers/all-MiniLM-L6-v2`) and indexes it in an in-memory FAISS store |
| `/chat` | GET/POST | RAG chat over the indexed PDF(s): retrieves the top-3 relevant chunks and asks Gemini to answer from that context |
| `/pdf_chat` | GET | Upload screen for the PDF chat flow |
| `/essay_rubric` | GET/POST | Form to submit a grading rubric |
| `/essay_grading` | POST | Grades a submitted essay (typed or PDF) against the stored rubric via Gemini |

## Approach

Retrieval is a hand-rolled closure (`get_conversation_chain`), not a LangChain chain object — it does a similarity search against the FAISS store and stuffs the results into a prompt sent directly to `google.generativeai`. Embeddings run locally via HuggingFace `sentence-transformers`; only generation calls Gemini's API.

## Technologies Used

Flask, google-generativeai (Gemini), LangChain (text splitting, FAISS wrapper), HuggingFace `sentence-transformers`, PyPDF2, FAISS.

## Setup & Running Locally

```bash
pip install -r requirements.txt
```

Create a `.env` file in this folder:

```
GEM_API_KEY=your_gemini_api_key
```

```bash
python app.py
```

## Key Learnings

- Wiring a PDF-ingestion → chunk → embed → retrieve → generate pipeline by hand, without a prebuilt LangChain chain.
- Serving several distinct LLM-backed features (chat, RAG, grading) from one Flask app with shared global state.

## Known Issues (found during repository cleanup)

- **`app.py` previously contained an unresolved Git merge conflict** — two entirely unrelated apps (an old sklearn breast-cancer predictor and this Gemini/RAG app) were both committed under conflict markers, making the file a syntax error that couldn't run. The conflict has been resolved by keeping only the Gemini/RAG app, which is what the templates and `requirements.txt` here actually support.
- **A live Gemini API key was hardcoded in `app.py`** (and reused in `resume-analyst-bot`). It has been replaced with `os.getenv("GEM_API_KEY")` loaded via `python-dotenv`. **This key is already public in the repository's Git history and should be revoked/rotated in Google AI Studio regardless of this fix.**
- `requirements.txt` was saved as UTF-16 and unparsable by `pip`; it has been re-saved as plain UTF-8 with the same package list.
- Five duplicate, unused HTML files sat at the project root (Flask only reads from `templates/`) and have been removed.
- `requirements.txt` still lists `scikit-learn`, `joblib`, `openai`, and `langchain-openai`, which nothing in this app imports — leftovers from the merge conflict / earlier experimentation. Left as-is since trimming them wasn't part of this reorganization; safe to prune later.
