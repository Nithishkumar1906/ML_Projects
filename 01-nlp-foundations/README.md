# 01 · NLP Foundations

Classical and transformer-based NLP: text preprocessing, POS/NER tagging, lexicon-based sentiment analysis, bag-of-words classification, and pretrained BERT/Transformer pipelines.

| Notebook | Description | Key Concepts |
| --- | --- | --- |
| [text-preprocessing-pipeline.ipynb](./text-preprocessing-pipeline.ipynb) | Cleans and normalizes a TripAdvisor restaurant-reviews dataset (lowercasing, tokenization, stemming vs. lemmatization) | NLTK, tokenization, stemming, lemmatization |
| [pos-ner-tagging.ipynb](./pos-ner-tagging.ipynb) | POS tagging and Named Entity Recognition on synthetic text and a BBC News dataset, with displaCy visualization | spaCy, POS tagging, NER |
| [lexicon-sentiment-analysis.ipynb](./lexicon-sentiment-analysis.ipynb) | Rule-based sentiment scoring with TextBlob and VADER, applied to book-review titles | Lexicon-based sentiment, TextBlob, VADER |
| [sentiment-classification-logreg-nb-svm.ipynb](./sentiment-classification-logreg-nb-svm.ipynb) | Compares Logistic Regression, Naive Bayes, and SGD/SVM on a small hand-written sentiment set (bag-of-words) | CountVectorizer, Logistic Regression, Naive Bayes, SVM |
| [fake-news-nlp-classification.ipynb](./fake-news-nlp-classification.ipynb) | End-to-end pipeline (cleaning, POS/NER, VADER, bag-of-words classification) on a PolitiFact-style fact-check dataset | Regex cleaning, n-grams, multiclass classification |
| [bert-question-answering.ipynb](./bert-question-answering.ipynb) | Extractive Q&A with a SQuAD-finetuned BERT model, plus a small FAQ-bot demo | BERT, extractive QA, span extraction |
| [huggingface-transformers-pipeline.ipynb](./huggingface-transformers-pipeline.ipynb) | Tour of HuggingFace `pipeline()` (sentiment, NER, zero-shot) plus manual tokenizer/model usage | Transformers pipelines, zero-shot classification |

**Note:** several notebooks load local CSVs (`TA_restaurants_curated.csv`, `Fake_or_Real.csv`, `Book_reviews.csv`, `bbc_news.csv`) that are not committed to this repo — supply your own copy to re-run those cells.
