import nltk
nltk.download ()
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

from nltk.stem import PorterStemmer
ps = PorterStemmer()


from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer()

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# tokenization 
sentence_data = "i'm the better progammer than you,because I am a python developer."

# sentence_data = "The First sentence is about Python. The Second: about Django. You can learn Python,Django and Data Ananlysis here. "
words = word_tokenize(sentence_data)

# stop words 
stop_words = set(stopwords.words('english'))
filtered_sentence = []
 
for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)
 
print(words)
print(filtered_sentence)

#  stemming 
  
for w in filtered_sentence:
    print(w, " : ", ps.stem(w))

print("lemantization")
for w in filtered_sentence:
    print(w,":",lemmatizer.lemmatize(w,pos ="a"))