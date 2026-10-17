import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import sys

# بارگذاری داده
df = pd.read_json("dataset_labeled.jsonl", lines=True)
X, y = df['text'], df['label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# آموزش Linear SVM
pipe = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=2, max_df=0.9)),
    ("clf", LinearSVC(class_weight='balanced', max_iter=2000))
])
pipe.fit(X_train, y_train)
y_pred = pipe.predict(X_test)

# چاپ گزارش
report = classification_report(y_test, y_pred, digits=4)
accuracy = accuracy_score(y_test, y_pred)

print("=" * 70)
print("Classification Report - Linear SVM")
print("=" * 70)
print(report)
print(f"Overall Accuracy: {accuracy:.4f}")

# ذخیره در فایل متنی
with open('classification_report.txt', 'w', encoding='utf-8') as f:
    f.write("Classification Report - Linear SVM\n")
    f.write("=" * 70 + "\n")
    f.write(report)
    f.write(f"\nOverall Accuracy: {accuracy:.4f}\n")

print("\n✅ ذخیره شد: classification_report.txt")