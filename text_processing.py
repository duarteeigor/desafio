import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')


def processText(text):
    text = text.lower()

    text = re.sub(r'[^a-záéíóúâêîôûãõç\s]', '', text)

    tokens = text.split()

    stop_words = set(stopwords.words('portuguese'))
    tokens = [word for word in tokens if word not in stop_words]

    formated_text = ' '.join(tokens)

    return formated_text
