import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# خواندن داده
import os
path = "data/train.jsonl" if os.path.exists("data/train.jsonl") else "data/data/train.jsonl"
df = pd.read_json(path, lines=True)

df['text'] = df['question'] + " " + df['answer']

# کلیدواژه‌های نهایی (۷ کلاس)
keywords = {
    "phishing":      ["فیشینگ", "ایمیل جعلی", "لینک مخرب"],
    "vishing":       ["ویشینگ", "فیشینگ صوتی", "تماس تلفنی"],
    "smishing":      ["اسمیشینگ", "پیامک", "SMS"],
    "baiting":       ["بیتینگ", "USB", "فلش", "Rubber Ducky"],
    "impersonation": ["جعل هویت", "جا زدن", "جعل هویت مدیرعامل"],
    "scareware":     ["هراس‌افزار", "پاپ‌آپ", "ویروس جعلی"],
    "tech_support":  ["پشتیبانی فنی", "FTC", "پشتیبانی جعلی"],
}

# برچسب‌گذاری: اولین کلاسی که تطابق داشته باشه
def assign_label(text):
    for label, words in keywords.items():
        for w in words:
            if w in text:
                return label
    return None

df['label'] = df['text'].apply(assign_label)

# آمار قبل از حذف
print("=" * 55)
print("توزیع کلاس‌ها قبل از پاک‌سازی:")
print("=" * 55)
print(df['label'].value_counts(dropna=False))

# حذف رکوردهای بدون برچسب
df_clean = df.dropna(subset=['label']).copy()
print(f"\nتعداد بعد از حذف بدون‌برچسب: {len(df_clean)}")

# حذف کلاس‌های نادر (کمتر از 20 نمونه)
counts = df_clean['label'].value_counts()
valid_labels = counts[counts >= 20].index.tolist()
df_final = df_clean[df_clean['label'].isin(valid_labels)].copy()

print(f"کلاس‌های نهایی: {valid_labels}")
print(f"تعداد نهایی: {len(df_final)}")
print(f"\nتوزیع نهایی:")
print(df_final['label'].value_counts())

# تقسیم train/test (Stratified)
X = df_final['text']
y = df_final['label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\nTrain: {len(X_train)}  |  Test: {len(X_test)}")

# ذخیره
df_final.to_json("dataset_labeled.jsonl", orient="records", lines=True, force_ascii=False)
print("\n✅ ذخیره شد در dataset_labeled.jsonl")