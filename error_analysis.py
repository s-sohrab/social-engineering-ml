import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# خواندن داده
df = pd.read_json("dataset_labeled.jsonl", lines=True)
X, y = df['text'], df['label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# بهترین مدل (SVM)
pipe = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=2, max_df=0.9)),
    ("clf", LinearSVC(class_weight='balanced', max_iter=2000))
])
pipe.fit(X_train, y_train)
y_pred = pipe.predict(X_test)

# 1. نمونه‌های اشتباه
print("=" * 70)
print("نمونه‌های اشتباه‌پیش‌بینی‌شده:")
print("=" * 70)

errors = X_test[y_pred != y_test]
true_labels = y_test[y_pred != y_test]
pred_labels = pd.Series(y_pred, index=y_test.index)[y_pred != y_test]

for i in range(min(10, len(errors))):
    print(f"\n--- نمونه {i+1} ---")
    print(f"متن: {errors.iloc[i][:200]}...")
    print(f"برچسب واقعی: {true_labels.iloc[i]}")
    print(f"پیش‌بینی:    {pred_labels.iloc[i]}")

# 2. Confusion Matrix
labels = sorted(y.unique())
cm = confusion_matrix(y_test, y_pred, labels=labels)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=labels, yticklabels=labels)
plt.xlabel('پیش‌بینی')
plt.ylabel('واقعی')
plt.title('Confusion Matrix - Linear SVM')
plt.tight_layout()
plt.savefig('confusion_matrix.png', dpi=150)
print("\n✅ نمودار ذخیره شد: confusion_matrix.png")

# 3. کلمات مهم هر کلاس
vectorizer = pipe.named_steps['tfidf']
clf = pipe.named_steps['clf']
feature_names = vectorizer.get_feature_names_out()

print("\n" + "=" * 70)
print("Top-10 کلمات مهم هر کلاس:")
print("=" * 70)

for i, label in enumerate(labels):
    coefs = clf.coef_[i]
    top_idx = np.argsort(coefs)[-10:][::-1]
    top_words = [feature_names[j] for j in top_idx]
    print(f"\n{label}: {' | '.join(top_words)}")

# 4. ذخیره نتایج برای مقاله
df_results = pd.DataFrame({
    'text': X_test.values,
    'true': y_test.values,
    'pred': y_pred
})
df_results.to_csv('test_predictions.csv', index=False, encoding='utf-8-sig')
print("\n✅ نتایج ذخیره شد: test_predictions.csv")