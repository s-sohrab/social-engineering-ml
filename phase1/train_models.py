import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix, f1_score
from sklearn.model_selection import train_test_split

# خواندن داده برچسب‌خورده
df = pd.read_json("dataset_labeled.jsonl", lines=True)
X = df['text']
y = df['label']

# تقسیم (Stratified)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ۴ مدل با Pipeline (TF-IDF داخل Pipeline → بدون Leakage)
models = {
    "Naive Bayes":    MultinomialNB(),
    "Logistic Reg":   LogisticRegression(max_iter=1000, class_weight='balanced'),
    "Linear SVM":     LinearSVC(class_weight='balanced', max_iter=2000),
    "Random Forest":  RandomForestClassifier(n_estimators=200, class_weight='balanced', random_state=42),
}

# Cross-Validation روی train
print("=" * 60)
print(f"{'مدل':<18} {'CV Macro-F1':<18} {'Std':<10}")
print("=" * 60)

results = {}
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

for name, clf in models.items():
    pipe = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=2, max_df=0.9)),
        ("clf", clf)
    ])
    scores = cross_val_score(pipe, X_train, y_train, cv=cv, scoring="f1_macro")
    results[name] = scores
    print(f"{name:<18} {scores.mean():<18.4f} {scores.std():<10.4f}")

# آموزش نهایی روی کل train و ارزیابی روی test
print("\n" + "=" * 60)
print("ارزیابی روی Test Set (دست‌نخورده):")
print("=" * 60)

best_name = max(results, key=lambda k: results[k].mean())
print(f"بهترین مدل بر اساس CV: {best_name}\n")

best_pipe = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=2, max_df=0.9)),
    ("clf", models[best_name])
])
best_pipe.fit(X_train, y_train)
y_pred = best_pipe.predict(X_test)

print("Classification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print(f"\nMacro-F1 روی Test: {f1_score(y_test, y_pred, average='macro'):.4f}")