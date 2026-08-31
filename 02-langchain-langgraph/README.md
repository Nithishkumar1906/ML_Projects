# 02 · LangChain & LangGraph

Chain composition (LCEL/Runnables), output parsing, document loading/chunking, embeddings with Pinecone, and LangGraph chatbots with short- and long-term memory.

| Notebook | Description | Key Concepts |
| --- | --- | --- |
| [langchain-chat-model-basics.ipynb](./langchain-chat-model-basics.ipynb) | Basic chat model invocation with `HumanMessage`/`SystemMessage` | Chat model roles |
| [lcel-basics.ipynb](./lcel-basics.ipynb) | Prompt → model → parser chain with `.invoke()`, `.batch()`, `.stream()` | LangChain Expression Language (LCEL) |
| [lcel-chained-pipelines.ipynb](./lcel-chained-pipelines.ipynb) | Two-step reasoning chain plus `RunnablePassthrough`/`RunnableLambda` examples | Chained LCEL pipelines, Runnables |
| [langchain-runnables.ipynb](./langchain-runnables.ipynb) | Composes the same multi-step chain into a single combined Runnable with graph introspection | Runnable composition, chain graphs |
| [langchain-output-parsers.ipynb](./langchain-output-parsers.ipynb) | Structured output parsing (`CommaSeparatedListOutputParser`) | Output parsers |
| [pdf-docx-loading-splitting.ipynb](./pdf-docx-loading-splitting.ipynb) | Loads and chunks a PDF/DOCX with different text splitters | Document loaders, text splitting |
| [embeddings-pinecone-search.ipynb](./embeddings-pinecone-search.ipynb) | Encodes a course catalog with sentence-transformers and indexes/queries it in Pinecone | Embeddings, semantic search |
| [pinecone-setup.ipynb](./pinecone-setup.ipynb) | Pinecone index administration (create/list/delete, upsert) | Vector database setup |
| [langgraph-basics.ipynb](./langgraph-basics.ipynb) | Single-node chatbot graph extended into a multi-turn Q&A loop | StateGraph, nodes/edges, conditional routing |
| [langgraph-short-term-memory.ipynb](./langgraph-short-term-memory.ipynb) | In-memory, thread-scoped conversation memory | `InMemorySaver` checkpointing |
| [langgraph-long-term-memory.ipynb](./langgraph-long-term-memory.ipynb) | SQLite-backed persistent memory with a summarization node | `SqliteSaver`, conversation summarization |
| [local-huggingface-llm-langchain.ipynb](./local-huggingface-llm-langchain.ipynb) | Runs a local `flan-t5-base` model as a LangChain LLM (no API key) | HuggingFace pipeline as LangChain LLM |

Most notebooks call an LLM via Groq's OpenAI-compatible endpoint (`llama3-70b-8192`).

**⚠️ Security note:** several notebooks in this folder (`lcel-basics`, `langgraph-basics`, `langchain-chat-model-basics`, `langgraph-long-term-memory`, `langchain-output-parsers`, `pdf-docx-loading-splitting`, `lcel-chained-pipelines`, `langgraph-short-term-memory`) hardcode a Groq API key directly in a code cell. This key is already committed to Git history — rotate/revoke it and switch to `python-dotenv` + a `.env` file before treating this repo as public.
