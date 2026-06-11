# evaluate.py

import pandas as pd
import joblib
import seaborn as sns
import matplotlib.pyplot as plt

from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

print("Loading saved models and data...")

lr_model = joblib.load("models/logistic_regression.pkl")
dt_model = joblib.load("models/decision_tree.pkl")

x_train_tfidf, x_test_tfidf, y_train, y_test = joblib.load(
    "models/split_matrices.pkl"
)

data = joblib.load("models/processed_dataframe.pkl")

# Class distribution
print("Showing class distribution...")

plt.figure(figsize=(6, 4))
sns.countplot(data=data, x="class")
plt.title("Class Distribution")
plt.show()

# Word cloud for real news
print("Creating word cloud for real news...")

real_text = " ".join(
    data[data["class"] == 1]["text"].astype(str)
)

wordcloud = WordCloud(width=800, height=400)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud.generate(real_text))
plt.axis("off")
plt.title("Real News Word Cloud")
plt.show()

# Word cloud for fake news
print("Creating word cloud for fake news...")

fake_text = " ".join(
    data[data["class"] == 0]["text"].astype(str)
)

wordcloud = WordCloud(width=800, height=400)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud.generate(fake_text))
plt.axis("off")
plt.title("Fake News Word Cloud")
plt.show()

# Most common words
print("Finding common words...")

def get_top_words(corpus, n):
    vectorizer = CountVectorizer()

    bag = vectorizer.fit_transform(corpus)

    word_count = bag.sum(axis=0)

    words = [
        (word, word_count[0, index])
        for word, index in vectorizer.vocabulary_.items()
    ]

    words = sorted(words, key=lambda x: x[1], reverse=True)

    return words[:n]

top_words = get_top_words(data["text"], 20)

df = pd.DataFrame(top_words, columns=["Word", "Count"])

df.plot(
    x="Word",
    y="Count",
    kind="bar",
    figsize=(10, 5)
)

plt.title("Top 20 Words")
plt.tight_layout()
plt.show()

# Accuracy scores
print("\nModel Results")
print("-" * 30)

lr_train = accuracy_score(
    y_train,
    lr_model.predict(x_train_tfidf)
)

lr_test = accuracy_score(
    y_test,
    lr_model.predict(x_test_tfidf)
)

dt_train = accuracy_score(
    y_train,
    dt_model.predict(x_train_tfidf)
)

dt_test = accuracy_score(
    y_test,
    dt_model.predict(x_test_tfidf)
)

print("Logistic Regression Train Accuracy:", lr_train)
print("Logistic Regression Test Accuracy :", lr_test)

print("Decision Tree Train Accuracy:", dt_train)
print("Decision Tree Test Accuracy :", dt_test)

# Confusion matrix
print("Showing confusion matrix...")

predictions = dt_model.predict(x_test_tfidf)

cm = confusion_matrix(y_test, predictions)

display = ConfusionMatrixDisplay(cm)

display.plot()

plt.title("Decision Tree Confusion Matrix")
plt.show()