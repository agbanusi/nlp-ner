# nlp-ner
This program takes-in data in picture or text format, determines what it is, extract the text and get the amount of errors 
in the document, also outputs the name of the company and location of the address found in the picture or text.
Dependencies:
nltk(stopwords, punkt tokenizer) for the sub-dependencies: python -m nltk.downloader punkt, python -m nltk.downloader stopwords
gingerit
pillow
spacy   sub-dependency: python -m spacy download en
pytesseract (python wrapper)
tesseract-ocr.exe gotten from https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20191010.exe
pytesseract.pytesseract.tesseract_cmd = Installed loaction/folder


