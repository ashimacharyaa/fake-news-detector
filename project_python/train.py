# train.py
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from utils import preprocess_text

print("Step 1: Reading News dataset...")
data = pd.read_csv('News.csv', index_col=0)

print("Step 2: Merging 'title' and 'text' columns for combined contextual focus...")
data['text'] = data['title'] + " " + data['text']

print("Step 3: Dropping unnecessary metadata tracking columns...")
data = data.drop(["title", "subject", "date"], axis=1).dropna()

print("Step 4: Shuffling dataset entries...")
data = data.sample(frac=1, random_state=42).reset_index(drop=True)

print("Step 5: Executing text scrubbing filters...")
data['text'] = preprocess_text(data['text'].values)

print("Step 6: Fragmenting data into Train and Test splits...")
x_train, x_test, y_train, y_test = train_test_split(
    data['text'], data['class'], test_size=0.25, random_state=42
)

print("Step 7: Transforming text corpus strings into numerical TF-IDF distributions...")
# We restrict max_features slightly to reduce data overfitting natively
vectorization = TfidfVectorizer(max_features=8000)
x_train_tfidf = vectorization.fit_transform(x_train)
x_test_tfidf = vectorization.transform(x_test)


# ==========================================
# CHANGE 1: REGULARIZATION (LOGISTIC REGRESSION)
# ==========================================
print("\nStep 8: Training Regularized Logistic Regression Model...")
# Lowering C from 1.0 to 0.01 applies a mathematical "brake"
# This shrinks the vocabulary coefficients and prevents 100% flat confidence bias
lr_model = LogisticRegression(C=0.01, max_iter=1000)
lr_model.fit(x_train_tfidf, y_train)


# ==========================================
# CHANGE 2: FEATURE PRUNING (DECISION TREE PREPARATION)
# ==========================================
print("\nStep 9: Identifying and Pruning top 100 overfitted shortcut words...")
# We use the regularized Logistic Regression weights to find the absolute most biased words
importance = lr_model.coef_[0]
feature_names = vectorization.get_feature_names_out()

# Pair words with their absolute mathematical weights and sort them
word_importance = sorted(zip(feature_names, importance), key=lambda x: abs(x[1]), reverse=True)
top_100_shortcuts = [word for word, weight in word_importance[:100]]

print(f"Top 5 pruned shortcut words: {top_100_shortcuts[:5]}")

# Create a filtered training/testing matrix that zeroes out the columns of these 100 shortcut words
feature_indices_to_prune = [vectorization.vocabulary_[word] for word in top_100_shortcuts if word in vectorization.vocabulary_]

x_train_pruned = x_train_tfidf.copy()
x_test_pruned = x_test_tfidf.copy()

# Zero out the columns for pruned words so the Decision Tree cannot use them to "cheat"
for idx in feature_indices_to_prune:
    x_train_pruned[:, idx] = 0
    x_test_pruned[:, idx] = 0

print("Step 10: Training Decision Tree Classifier on Pruned Feature Matrix...")
dt_model = DecisionTreeClassifier(max_depth=15, random_state=42) # Added max_depth limit to stop overfitting
dt_model.fit(x_train_pruned, y_train)


print("\nStep 11: Exporting updated pipelines safely to disk storage...")
joblib.dump(vectorization, 'models/vectorizer.pkl')
joblib.dump(lr_model, 'models/logistic_regression.pkl')
joblib.dump(dt_model, 'models/decision_tree.pkl')
# We save the pruned matrices so evaluate.py reads the right data format
joblib.dump((x_train_tfidf, x_test_pruned, y_train, y_test), 'models/split_matrices.pkl')
joblib.dump(data, 'models/processed_dataframe.pkl')

print("\nPipeline execution complete! Run 'python evaluate.py' and 'streamlit run app.py' to observe the smoother probability distributions.")