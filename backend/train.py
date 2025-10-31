# train.py — small training pipeline to create model.pkl and vectorizer.pkl
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
from utils import clean_text
import os

TRUE_CSV = os.path.join('dataset','True.csv')
FAKE_CSV = os.path.join('dataset','Fake.csv')

def load_data():
    t = pd.read_csv(TRUE_CSV)
    f = pd.read_csv(FAKE_CSV)
    t['label'] = 1
    f['label'] = 0
    df = pd.concat([t, f], ignore_index=True)
    for col in ['text', 'content', 'title']:
        if col in df.columns:
            df['raw_text'] = df[col]
            break
    df = df[['raw_text', 'label']].dropna()
    return df

if __name__ == '__main__':
    df = load_data()
    df['clean'] = df['raw_text'].apply(clean_text)
    X = df['clean']
    y = df['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    vec = TfidfVectorizer(stop_words='english', max_df=0.7)
    X_train_vec = vec.fit_transform(X_train)
    X_test_vec = vec.transform(X_test)

    model = PassiveAggressiveClassifier(max_iter=1000)
    model.fit(X_train_vec, y_train)

    preds = model.predict(X_test_vec)
    print('Accuracy:', accuracy_score(y_test, preds))
    print(classification_report(y_test, preds))

    os.makedirs('model', exist_ok=True)
    joblib.dump(model, 'model/model.pkl')
    joblib.dump(vec, 'model/vectorizer.pkl')
    print('Saved model and vectorizer to model/')
