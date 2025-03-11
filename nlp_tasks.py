import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize, sent_tokenize

text = """Natural Language Toolkit (NLTK) is one of the largest Python 
libraries for performing various Natural Language Processing tasks. 
From rudimentary tasks such as text pre-processing to tasks like 
vectorized representation of text – NLTK’s API has covered everything."""

words = word_tokenize(text)
sentences = sent_tokenize(text)

print("Words:", words)
print("\nSentences:", sentences)
