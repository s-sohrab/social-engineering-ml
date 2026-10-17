import pandas as pd
import os

possible_paths = [
    "data/data/train.jsonl",
    "data/train.jsonl",
]
data_path = None
for p in possible_paths:
    if os.path.exists(p):
        data_path = p
        break

print(f"مسیر فایل: {data_path}")

df = pd.read_json(data_path, lines=True)

print(f"\nتعداد رکوردها: {len(df)}")
print(f"ستون‌ها: {df.columns.tolist()}")
print(f"\nنمونه اول:")
print(df.iloc[0])

print(f"\nمقادیر خالی:")
print(df.isnull().sum())