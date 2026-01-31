import nltk
import string
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')   
nltk.download('stopwords')
nltk.download('wordnet')

text = "The quick BROWN foxes... there are JUMPING over 10 lazy dogs!"

text = text.lower()

text = re.sub(r'\d+', '', text)

text = text.translate(str.maketrans('', '', string.punctuation))

text = re.sub(r'\s+', ' ', text).strip()

words = word_tokenize(text)

stop_words = set(stopwords.words('english'))
words = [w for w in words if w not in stop_words]

lemmatizer = WordNetLemmatizer()
words = [lemmatizer.lemmatize(w, pos='v') for w in words]
clean_words = [lemmatizer.lemmatize(w) for w in words]

print(clean_words)