# 06 · Applied GenAI & NLP

Later, more applied practicals: multimodal LLM assistants (chat + image + speech), HuggingFace pipeline/transformer fundamentals, LLM-based code translation, local quantized LLM inference, and a two-part sentiment-analysis project comparing classical ML, RNN-family models, and BERT.

| Notebook | Description | Key Concepts |
| --- | --- | --- |
| [huggingface-pipelines-overview.ipynb](./huggingface-pipelines-overview.ipynb) | Practice run through HuggingFace `pipeline()` across sentiment, NER, QA, summarization, translation, zero-shot, and generation | Transformers pipelines |
| [multimodal-flight-assistant-image-tts.ipynb](./multimodal-flight-assistant-image-tts.ipynb) | Flight-assistant chatbot extended with destination poster generation and spoken replies | Tool calling, text-to-image, text-to-speech |
| [text-to-image-generation-comparison.ipynb](./text-to-image-generation-comparison.ipynb) | Compares local Diffusers, HF Inference API, Replicate, and pollinations.ai for generating travel posters | Text-to-image generation backends |
| [python-to-cpp-code-translator.ipynb](./python-to-cpp-code-translator.ipynb) | Uses Gemini to translate/optimize Python snippets into C++, streamed into a Gradio UI | LLM code translation |
| [local-quantized-llm-gemma.ipynb](./local-quantized-llm-gemma.ipynb) | Runs a 4-bit quantized Gemma-2B-it model locally with streamed generation | Quantized local LLM inference (bitsandbytes) |

## Featured project: sentiment analysis, three ways

Two related notebooks benchmark the same tweet-sentiment task (Sentiment140 dataset) across increasingly sophisticated model families:

### [sentiment-rnn-lstm-gru-report.ipynb](./sentiment-rnn-lstm-gru-report.ipynb)

A "final report" style comparison of SimpleRNN, LSTM, and GRU for binary tweet sentiment classification, trained on ~917K cleaned samples (80/20 split), with a written deployment recommendation.

| Model | Accuracy | Positive-class F1 |
| --- | --- | --- |
| SimpleRNN | 0.8415 | 0.6822 |
| LSTM | 0.8504 | 0.6903 |
| **GRU** | **0.8505** | **0.6976** |

**Conclusion:** GRU recommended for deployment as the best speed/accuracy trade-off.

### [sentiment-analysis-classical-vs-deep-vs-bert.ipynb](./sentiment-analysis-classical-vs-deep-vs-bert.ipynb)

A broader benchmark on the same dataset, adding classical ML (TF-IDF + Logistic Regression, Linear SVM) and a fine-tuned DistilBERT alongside the RNN family.

| Model | Accuracy | Positive-class F1 |
| --- | --- | --- |
| Logistic Regression (TF-IDF) | 0.8457 | — |
| Linear SVM (TF-IDF) | 0.8447 | 0.61 |
| SimpleRNN | 0.8546 | — |
| LSTM | 0.8639 | — |
| GRU | 0.8619 | 0.67 |
| DistilBERT (fine-tuned, 50K sample) | 0.7538 | 0.6120 |

**Key learning:** in this setup, simpler sequence models (LSTM/GRU) outperformed a fine-tuned DistilBERT — likely due to the much smaller fine-tuning sample (50K vs. ~1M+ for the other models) and only 2 training epochs.

**Note:** both notebooks load `training.1600000.processed.noemoticon.csv` (Sentiment140) from a Colab path — the dataset is not included in this repo.

---

<sub>[Back to portfolio](../README.md) · [GitHub](https://github.com/Nithishkumar1906) · [LinkedIn](https://www.linkedin.com/in/nithish-kumar-m-s-04500626a)</sub>
