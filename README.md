# NER-DODF

A simple Flask web application for extracting named entities using the spaCy model

The dataset used is from DODF. The model was trained only with 24 DODF sentences to detect three types of entities:
pessoa, matrícula and ação (Spacy_custom_NER_model.ipynb)

How to run:

1 - git clone https://github.com/lindeberg25/ner-dodf.git

2 - python app.py

3 - Access the URL

To make testing easier, there are excerpts from DODF in test.txt. However, feel free to test with others.

Credit: this code was customized from https://github.com/susanli2016/Named-Entity-Extractor



