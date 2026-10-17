import pandas as pd

# بارگذاری داده
df = pd.read_json("phase2/data/attack_texts.jsonl", lines=True)

print("=" * 60)
print(f"تعداد کل متن‌های تولیدشده: {len(df)}")
print("=" * 60)

# توزیع کلاس‌ها
print("\nتوزیع کلاس‌ها:")
print(df['label'].value_counts())

# بررسی طول متن
df['text_len'] = df['attack_text'].str.len()
print(f"\nمیانگین طول متن: {df['text_len'].mean():.1f} کاراکتر")
print(f"حداقل: {df['text_len'].min()} | حداکثر: {df['text_len'].max()}")

# نمایش ۳ نمونه از هر کلاس
print("\n" + "=" * 60)
print("نمونه‌های تولیدشده:")
print("=" * 60)

for label in df['label'].unique():
    print(f"\n--- کلاس: {label} ---")
    samples = df[df['label'] == label].head(2)
    for i, row in samples.iterrows():
        print(f"متن: {row['attack_text'][:150]}...")
        print()
    