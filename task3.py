import string

text = """Let’s eat, Grandma! 
Grandma, Let’s eat! 
Silvia, Are you free tomorrow? 
Yes, I’m free on Saturday."""

cleaned_text = text.lower().translate(str.maketrans('', '', string.punctuation))

print("Cleaned Text:", cleaned_text)
