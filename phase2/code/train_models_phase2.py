import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix, f1_score, accuracy_score

# =====================================================
# بارگذاری داده فاز دوم
# =====================================================
df = pd.read_json("phase2/data/attack_texts.jsonl", lines=True)
X = df['attack_text']
y = df['label']

print("=" * 60)
print("فاز دوم: آموزش مدل‌ها روی متن‌های حمله تولیدشده")
print("=" * 60)
print(f"تعداد کل نمونه‌ها: {len(df)}")
print(f"توزیع کلاس‌ها:\n{y.value_counts()}\n")

# =====================================================
# تقسیم Train/Test (Stratified)
# =====================================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"Train: {len(X_train)} | Test: {len(X_test)}\n")

# =====================================================
# آموزش ۴ مدل با Pipeline (بدون Leakage)
# =====================================================
models = {
    "Naive Bayes":         MultinomialNB(),
    "Logistic Regression": LogisticRegression(max_iter=1000, class_weight='balanced'),
    "Linear SVM":          LinearSVC(class_weight='balanced', max_iter=2000),
    "Random Forest":       RandomForestClassifier(n_estimators=200, class_weight='balanced', random_state=42),
}

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
results = {}

print("=" * 60)
print(f"{'مدل':<20} {'Mean Macro-F1':<15} {'Std':<10}")
print("=" * 60)

for name, clf in models.items():
    pipe = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=2, max_df=0.9)),
        ("clf", clf)
    ])
    scores = cross_val_score(pipe, X_train, y_train, cv=cv, scoring="f1_macro")
    results[name] = scores
    print(f"{name:<20} {scores.mean():<15.4f} {scores.std():<10.4f}")

# =====================================================
# ارزیابی نهایی بهترین مدل (Linear SVM)
# =====================================================
best_pipe = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=2, max_df=0.9)),
    ("clf", LinearSVC(class_weight='balanced', max_iter=2000))
])
best_pipe.fit(X_train, y_train)
y_pred = best_pipe.predict(X_test)

print("\n" + "=" * 60)
print("ارزیابی نهایی Linear SVM روی Test (فاز دوم)")
print("=" * 60)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"Macro-F1: {f1_score(y_test, y_pred, average='macro'):.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# =====================================================
# ذخیره نتایج
# =====================================================
import json

results_summary = {
    "phase": "phase2",
    "n_samples": len(df),
    "n_train": len(X_train),
    "n_test": len(X_test),
    "cv_results": {k: {"mean": v.mean(), "std": v.std()} for k, v in results.items()},
    "best_model": "Linear SVM",
    "test_accuracy": accuracy_score(y_test, y_pred),
    "test_macro_f1": f1_score(y_test, y_pred, average='macro'),
}

with open("phase2/results/phase2_results.json", "w", encoding="utf-8") as f:
    json.dump(results_summary, f, ensure_ascii=False, indent=2)

print("\n✅ نتایج ذخیره شد: phase2/results/phase2_results.json")