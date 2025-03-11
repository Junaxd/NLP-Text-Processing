import re

text = """ @@Natural   Language Processing (NLP)!!!  is a    field of AI that  
focuses on  ...     
   enabling computers to understand,    interpret, & generate   human  
language.   
 NLP   includes  tasks like **tokenization, lemmatization,**  && 
sentiment analysis.     
 It  helps in   applications such as chatbots,   machine translation,  
and   voice assistants!!!   
 However,   cleaning text—removing   extra spaces, punctuations, && 
special $$$ characters—is crucial.     
 Without   preprocessing,  NLP models may not    perform    
accurately !!!     
 So,   can you clean this   messy text & make  it    structured???   """

cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove special characters
cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()  # Remove extra spaces

print("Cleaned Text:", cleaned_text)
