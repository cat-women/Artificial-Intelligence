import nltk
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer()

print("rocks :", lemmatizer.lemmatize("rocks"))
print("corpora :", lemmatizer.lemmatize("corpora"))
print("are :", lemmatizer.lemmatize("are", pos ="a"))
print("cooking :", lemmatizer.lemmatize("cooking"))
  
# a denotes adjective in "pos"
print("better :", lemmatizer.lemmatize("better", pos ="a"))