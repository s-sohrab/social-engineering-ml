import pandas as pd

df = pd.read_json("data/train.jsonl", lines=True) if __import__("os").path.exists("data/train.jsonl") else pd.read_json("data/data/train.jsonl", lines=True)

# ترکیب سوال + پاسخ
df['text'] = df['question'] + " " + df['answer']

keywords = {
    "phishing":      ["فیشینگ", "ایمیل جعلی", "لینک مخرب"],
    "vishing":       ["ویشینگ", "فیشینگ صوتی", "تماس تلفنی"],
    "smishing":      ["اسمیشینگ", "پیامک", "SMS"],
    "baiting":       ["بیتینگ", "USB", "فلش", "Rubber Ducky"],
    "pretexting":    ["پیش‌متنسازی", "پیش متن", "سناریوی ساختگی"],
    "impersonation": ["جعل هویت", "جا زدن", "جعل هویت مدیرعامل"],
    "sextortion":    ["سکستورشن", "باج‌گیری جنسی", "اخاذی"],
    "scareware":     ["هراس‌افزار", "پاپ‌آپ", "ویروس جعلی"],
    "tailgating":    ["تیلگیتینگ", "پیگیبکینگ", "منطقه محدود"],
    "tech_support":  ["پشتیبانی فنی", "FTC", "پشتیبانی جعلی"],
}

print("=" * 55)
print(f"{'نوع حمله':<15} {'تعداد تطابق':<10}")
print("=" * 55)

for label, words in keywords.items():
    total = 0
    for w in words:
        total += df['text'].str.contains(w, case=False, na=False).sum()
    print(f"{label:<15} {total:<10}")