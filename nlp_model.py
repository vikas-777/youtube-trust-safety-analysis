import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

# Sample dataset (you can expand this)
data = {
    "text": [
        "This is a normal educational video",
        "Win free money now click here",
        "I hate this community",
        "Learn Python programming",
        "Violent fight video shocking",
        "Subscribe for free gifts",
        "Offensive and abusive content",
        "Tech tutorial for beginners"
    ],
    "label": [
        "Safe",
        "Spam",
        "Hate Speech",
        "Safe",
        "Violence",
        "Spam",
        "Hate Speech",
        "Safe"
    ]
}

df = pd.DataFrame(data)

# Convert text to features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print(classification_report(y_test, y_pred))

# Test example
sample = ["Free iPhone offer click now"]
sample_vec = vectorizer.transform(sample)
print("Prediction:", model.predict(sample_vec))
