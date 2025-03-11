import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

text = """The researchers are analyzing various datasets to study the effects 
of automation. They observed that automated systems perform tasks more 
efficiently than humans. Many industries have been adopting AI-driven 
solutions to improve productivity. Running complex algorithms helps in 
predicting future trends accurately. Several companies are investing in 
developing smarter and more adaptive models. Data scientists continuously 
refine their models to achieve better performance. The advancements in 
technology have transformed the way businesses operate."""

words = word_tokenize(text)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

stemmed_words = [stemmer.stem(word) for word in words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

print("Stemmed Words:", stemmed_words)
print("\nLemmatized Words:", lemmatized_words)
