import nltk
nltk.download('punkt')       # For tokenization
nltk.download('stopwords')   # For stopwords
nltk.download('wordnet')     # For WordNet lemmatizer
nltk.download('omw-1.4')     # For WordNet Lemmatizer's additional data
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import gensim
import re
import gensim.corpora as corpora
import pandas as pd

# Load Data
# Read csv file
data = pd.read_csv('news_articles.csv')
data.head()
data.info()

# Clean Data
articles =  data['content'].str.lower().apply(lambda x : re.sub(r"([^\w\s])","",x))

# Stopwords removal
en_stopwords =  stopwords.words('english')
articles  = articles.apply(lambda x :''.join([word for word in x.split() if word not in (en_stopwords)]))


# tokenize
articles = articles.apply(lambda x: word_tokenize)

# stemming (done for speed as we have a lot of text)
ps = PorterStemmer()
articles = articles.apply(lambda tokens: [ps.stem(token) for token in tokens])