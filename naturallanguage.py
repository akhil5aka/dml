import nltk 
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('Wordnet')
nltk.download('omw-1.4')
from nltk.tokenize import sent_tokenize,word_tokenize 
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer
from nltk.stem wordnet import WordNetLemmatizer
text="""hello mr.smith,how are you doing today? The weatheris great,and city is awesome.
The sky is pinkish-blue.you shouldn't eat cardboard"""
tokenized_word=word_tokenize(text)
print(tokenized_word)

stop_words=set(stopwords.words("english"))
print(stop_words)
filtered_word=[]
for w  in stop_word:
    if w not in stop_words:
        filtered_word.append(w)
print("Tokenized Sentence :",tokenized_word)
print("Filtered Sentence:",filtered_word)
ps = PorterStemmer()
stemmed__words=[]
for w in filtered_word:
    stemmed__words.append(ps.stem(w))
    print("Filtered Sentence:",filtered_word)
    print("Stemmed Sentence:",stemmed__words)
    lem = WodrNetLemmatizer()
    stem = porterStemmer()
    word = "flying"
    print("Lemmatized Word:",lem.lemmatize(word,"v"))
    print("Stemmed Word:",stem.stem(word))
