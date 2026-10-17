import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split

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

# استخراج کلمات مهم هر کلاس
vectorizer = pipe.named_steps['tfidf']
clf = pipe.named_steps['clf']
feature_names = vectorizer.get_feature_names_out()
classes = clf.classes_

# ساخت دیکشنری: کلاس → لیست ۱۰ کلمه برتر
top_words = {}
for i, label in enumerate(classes):
    coefs = clf.coef_[i]
    top_idx = np.argsort(coefs)[-10:][::-1]
    top_words[label] = [feature_names[j] for j in top_idx]

# ساخت DataFrame (سطر = رتبه، ستون = کلاس)
df_table = pd.DataFrame({
    label: words for label, words in top_words.items()
})
df_table.index = [f"رتبه {i+1}" for i in range(10)]
df_table.index.name = "Rank"

print("\n" + "=" * 80)
print("جدول Top-10 کلمات مهم هر کلاس (Linear SVM)")
print("=" * 80)
print(df_table.to_string())

# ذخیره در CSV (برای استفاده در گزارش)
df_table.to_csv('top10_words_per_class.csv', encoding='utf-8-sig')

# ذخیره در Excel (اگر خواستید به Word منتقل کنید)
try:
    df_table.to_excel('top10_words_per_class.xlsx')
    print("\n✅ ذخیره شد: top10_words_per_class.xlsx")
except ImportError:
    print("\n⚠️ برای ذخیره Excel، openpyxl رو نصب کنید: pip install openpyxl")

print("✅ ذخیره شد: top10_words_per_class.csv")