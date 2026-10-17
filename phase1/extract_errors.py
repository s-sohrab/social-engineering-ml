import pandas as pd
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
y_pred = pipe.predict(X_test)

# استخراج نمونه‌های اشتباه
df_errors = pd.DataFrame({
    'text': X_test.values,
    'true_label': y_test.values,
    'predicted_label': y_pred,
})
df_errors = df_errors[df_errors['true_label'] != df_errors['predicted_label']].copy()

# مرتب‌سازی بر اساس نوع خطا
df_errors = df_errors.sort_values(['true_label', 'predicted_label']).reset_index(drop=True)

print("=" * 80)
print(f"تعداد نمونه‌های اشتباه: {len(df_errors)}")
print("=" * 80)

# چاپ نمونه‌ها
for i, row in df_errors.iterrows():
    print(f"\n--- خطای {i+1} ---")
    print(f"واقعی: {row['true_label']}  |  پیش‌بینی: {row['predicted_label']}")
    print(f"متن: {row['text'][:250]}...")
    print("-" * 80)

# ذخیره در CSV
df_errors.to_csv('misclassified_samples.csv', index=False, encoding='utf-8-sig')
print(f"\n✅ ذخیره شد: misclassified_samples.csv")

# ذخیره در Excel (اگر openpyxl نصب باشه)
try:
    df_errors.to_excel('misclassified_samples.xlsx', index=False)
    print("✅ ذخیره شد: misclassified_samples.xlsx")
except ImportError:
    pass