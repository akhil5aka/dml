import nltk 
from nltk.tokenize import sent_tokenize,word_tokenize 
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')
text="""hello mr.smith,how are you doing today? The weatheris great,and city is awesome.The sky is pinkish-blue.you shouldn't eat cardboard"""
tokenized_word=word_tokenize(text)
print(tokenized_word)
stopwords
stop_words=set(stopwords.words("english"))
print(stop_words)
filtered_word=[]
for w  in stop_words:
    if w not in stop_words:
        filtered_word.append(w)
print("tokenized sentence :",tokenized_word)
print("Filtered sentence:",filtered_word)
ps = PorterStemmer()
stemmed__words=[]
for w in filtered_word:
    stemmed__words.append(ps.stem(w))
    print("Filtered Sentence:",filtered_word)
    print("Stemmed sentence:",stemmed__words)