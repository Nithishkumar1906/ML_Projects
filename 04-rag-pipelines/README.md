# 04 · RAG Pipelines & Evaluation

A progression of Retrieval-Augmented Generation pipelines over the same source PDF (a RAG research paper), from a basic FAISS setup through a local/offline variant, a Pinecone-backed variant, and a dedicated evaluation notebook using multiple automated metrics.

| Notebook | Description | Key Concepts |
| --- | --- | --- |
| [rag-basic-pdf-qa.ipynb](./rag-basic-pdf-qa.ipynb) | Baseline RAG: load PDF → chunk → embed (Google) → FAISS → `ConversationalRetrievalChain` with Gemini | RAG fundamentals, FAISS |
| [rag-local-ollama-perplexity.ipynb](./rag-local-ollama-perplexity.ipynb) | Local/offline RAG served by Ollama (gemma3:1b, tinyllama), plus a separate GPT-2 perplexity demo | Local LLM serving, perplexity as a text-quality metric |
| [rag-pinecone-vector-store.ipynb](./rag-pinecone-vector-store.ipynb) | Same RAG pipeline rebuilt on a Pinecone index instead of FAISS | Managed vector database retrieval |
| [rag-evaluation-ragas-bleu-rouge.ipynb](./rag-evaluation-ragas-bleu-rouge.ipynb) | Evaluates RAG answers against a hand-labeled Q&A set with RAGAS, BLEU, ROUGE-1, and BERTScore | RAG evaluation metrics |

**Note:** `model-training.ipynb`, previously a stray, unrelated classical-ML notebook in this folder (a breast-cancer classifier), has been moved to [`projects/cancer-prediction-app/`](../projects/cancer-prediction-app/) — it's the training notebook behind that app's `model.pkl`, not part of the RAG progression.

**⚠️ Security note:** `rag-basic-pdf-qa.ipynb`, `rag-pinecone-vector-store.ipynb`, and `rag-evaluation-ragas-bleu-rouge.ipynb` hardcode API keys (Google, Pinecone, Groq) directly in code cells. These are already committed to Git history — rotate/revoke them and switch to `python-dotenv` before treating this repo as public.
