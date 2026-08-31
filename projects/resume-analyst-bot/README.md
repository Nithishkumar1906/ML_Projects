# Resume Analyst Bot

## Overview

A Flask app that summarizes an uploaded resume and answers free-form questions about it, using a FAISS-backed retrieval pipeline and Google's Gemini API.

## Features

| Route | Method | Description |
| --- | --- | --- |
| `/` | GET | Resume upload form |
| `/upload` | POST | Saves the PDF, extracts text (`PyPDF2`), chunks it (`CharacterTextSplitter`, 2000/200), embeds it (`HuggingFaceEmbeddings`), builds a FAISS index (saved to `vector_index/`), and asks Gemini for a structured summary (objective, skills, experience, education, achievements) |
| `/ask` | GET/POST | Retrieves the top-3 chunks relevant to a typed question and asks Gemini to answer from that context |

## Approach

Classic RAG: PDF → text extraction → chunking → local embeddings → FAISS similarity search → Gemini generation. The index is rebuilt and overwritten on every upload, so only one resume's index exists on disk at a time.

## Technologies Used

Flask, google-generativeai (Gemini), LangChain (text splitting, FAISS/embeddings wrappers), HuggingFace `sentence-transformers`, PyPDF2, FAISS.

## Setup & Running Locally

```bash
pip install -r requirements.txt
```

Create a `.env` file in this folder:

```
GEMINI_API_KEY=your_gemini_api_key
```

```bash
python app.py
```

## Key Learnings

- Building a resume-specific RAG pipeline (upload → index → summarize / Q&A) from scratch with Flask + FAISS.
- Persisting and reloading a vector store across requests with `save_local` / `load_local`.

## Known Issues (found during repository cleanup)

- **A live Gemini API key was hardcoded in `app.py`** (the same key reused in `chat-ai-assistant`). It has been replaced with `os.getenv("GEMINI_API_KEY")` loaded via `python-dotenv`. **This key is already public in the repository's Git history and should be revoked/rotated in Google AI Studio regardless of this fix.**
- `requirements.txt` was saved as UTF-16 and unparsable by `pip`; it has been re-saved as plain UTF-8 with the same package list.
- `uploads/` contains the developer's own resume files (real name and history) and `vector_index/` contains a FAISS index built from one of them. Both are now covered by `.gitignore` going forward; the tracked `vector_index/` files have been removed as regenerable build artifacts. **The resume files in `uploads/` are still present in Git history and were not deleted here — recommend deciding whether to purge them from history before treating this repo as public.**
- `templates/query_results.html` exists but is not referenced by any route in `app.py` — likely a leftover from earlier development.
