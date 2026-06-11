
import re
from tqdm import tqdm
import nltk
from nltk.corpus import stopwords

# download stopwords if not already downloaded
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def preprocess_text(text_data):
    cleaned_text = []

    for text in tqdm(text_data):
        # remove punctuation
        text = re.sub(r'[^\w\s]', '', str(text))

        # convert to lowercase and remove stopwords
        words = text.lower().split()

        filtered_words = []
        for word in words:
            if word not in stop_words:
                filtered_words.append(word)

        text = " ".join(filtered_words)
        cleaned_text.append(text)

    return cleaned_text