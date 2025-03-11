import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = """Natural Language Toolkit (NLTK) works as a powerful Python 
library that a wide range of tools for Natural Language Processing 
(NLP). From fundamental tasks like text pre-processing to more 
advanced operations such as semantic reasoning, NLTK provides a 
versatile API that caters to the diverse needs of language-related 
tasks."""

stop_words = set(stopwords.words('english'))
words = word_tokenize(text)
filtered_text = [word for word in words if word.lower() not in stop_words]

print("Filtered Text:", filtered_text)
