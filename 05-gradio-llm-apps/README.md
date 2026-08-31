# 05 · Gradio & LLM Apps

Interactive AI apps built with Gradio, Gemini, and web scraping: streaming chatbots, tool-calling, multi-agent dialogue, and an LLM-powered brochure generator.

| Notebook | Description | Key Concepts |
| --- | --- | --- |
| [gradio-sales-chatbot.ipynb](./gradio-sales-chatbot.ipynb) | Streaming Gradio chatbot for a clothing store that steers customers toward sale items | Gradio `ChatInterface`, streaming |
| [gradio-flight-assistant-tool-calling.ipynb](./gradio-flight-assistant-tool-calling.ipynb) | Airline assistant chatbot with function/tool-calling for ticket price lookups | Tool calling / function calling |
| [gemini-ollama-debate-streaming.ipynb](./gemini-ollama-debate-streaming.ipynb) | Two LLMs (Gemini and local Ollama) debate a topic, streamed live into a Gradio Blocks UI | Multi-agent dialogue, streaming Blocks UI |
| [web-summarization-gemini.ipynb](./web-summarization-gemini.ipynb) | Scrapes a webpage and summarizes it with Gemini, plus a small link-scraping/email-subject exercise | Web scraping, summarization |
| [web-scraping-brochure-generator.ipynb](./web-scraping-brochure-generator.ipynb) | Scrapes a company site, uses Gemini (JSON mode) to pick relevant sub-pages, then streams a generated brochure | Structured LLM output, multi-step scraping pipeline |

**Note:** `gradio-flight-assistant-tool-calling.ipynb` and `web-summarization-gemini.ipynb` contain unfinished/buggy sections (a mismatched tool function name in the former; a summarizer that ignores the scraped content in the latter) — kept as-is since they're learning exercises, not the final version of that idea (see `06-applied-genai-nlp` for the more complete flight-assistant iteration).
