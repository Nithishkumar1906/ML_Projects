# 03 · Deep Learning & Speech

CNNs for image classification (including transfer learning), RNN-family models (LSTM/GRU) for text generation, and applied speech processing (STT/TTS) with quantitative WER/CER evaluation.

| Notebook | Description | Key Concepts | Result |
| --- | --- | --- | --- |
| [cnn-fashion-mnist-binary.ipynb](./cnn-fashion-mnist-binary.ipynb) | Small CNN on a 2-class subset of Fashion-MNIST | CNN, binary image classification | training/eval code present; final accuracy not captured in saved output |
| [cnn-pneumonia-xray-classification.ipynb](./cnn-pneumonia-xray-classification.ipynb) | Custom CNN vs. VGG16 transfer learning on chest X-rays (NORMAL vs. PNEUMONIA) | CNN, transfer learning | Custom CNN 75.48% test acc · VGG16 transfer learning 91.03% test acc |
| [lstm-text-generation.ipynb](./lstm-text-generation.ipynb) | Word-level next-word prediction on a short inline paragraph | LSTM, sequence modeling | qualitative predictions only |
| [gru-text-generation.ipynb](./gru-text-generation.ipynb) | Same next-word-prediction exercise using a GRU | GRU, sequence modeling | qualitative predictions only |
| [pinecone-setup.ipynb](./pinecone-setup.ipynb) | Pinecone index administration and a toy vector upsert | Vector database setup | — |
| [speech-to-text-draft.ipynb](./speech-to-text-draft.ipynb) | Earlier pass: waveform/spectrogram visualization, Google STT vs. Whisper comparison | Speech-to-text, WER/CER | Google STT WER 0.45 · Whisper WER 0.15 |
| [speech-to-text-and-tts.ipynb](./speech-to-text-and-tts.ipynb) | Full version: STT comparison plus batch transcription (CSV export) and gTTS speech synthesis | Speech-to-text, text-to-speech | Whisper best performer (WER 0.15, CER 0.056) |

**Note:** speech notebooks use the developer's own local recordings, not a public dataset — audio files are not included in this repo.
