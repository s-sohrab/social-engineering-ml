import json
import requests
import time
import pandas as pd
from tqdm import tqdm

# =====================================================
# تنظیمات
# =====================================================
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:7b"
INPUT_FILE = "phase1/dataset_labeled.jsonl"
OUTPUT_FILE = "phase2/data/attack_texts.jsonl"

# =====================================================
# Prompt برای تولید متن حمله
# =====================================================
def build_prompt(question, answer, label):
    return f"""تو یک متخصص امنیت سایبری هستی. بر اساس اطلاعات زیر، یک متن واقعی حمله مهندسی اجتماعی به فارسی بنویس.

نوع حمله: {label}

اطلاعات زمینه:
سوال: {question}
پاسخ: {answer}

حالا یک متن واقعی حمله از نوع «{label}» به فارسی بنویس که:
1. شبیه یک پیام واقعی باشد (ایمیل، پیامک، یا متن تماس)
2. حداکثر ۳ جمله باشد
3. طبیعی و باورپذیر باشد
4. فقط متن حمله را بنویس، بدون توضیح اضافه

متن حمله:"""

# =====================================================
# تابع تولید متن با Ollama
# =====================================================
def generate_text(prompt):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.8,
                    "num_predict": 150,
                }
            },
            timeout=120
        )
        if response.status_code == 200:
            return response.json().get("response", "").strip()
        else:
            return None
    except Exception as e:
        print(f"خطا: {e}")
        return None

# =====================================================
# اجرای اصلی
# =====================================================
def main():
    print("=" * 60)
    print("شروع تولید متن‌های حمله (فاز دوم)")
    print("=" * 60)

    # بارگذاری دیتاست فاز اول
    df = pd.read_json(INPUT_FILE, lines=True)
    print(f"تعداد رکوردهای ورودی: {len(df)}")

    # نمونه‌گیری از هر کلاس (حداکثر ۵۰ نمونه از هر کلاس)
    samples = []
    for label in df['label'].unique():
        class_df = df[df['label'] == label].head(50)
        samples.append(class_df)
    
    df_sample = pd.concat(samples).reset_index(drop=True)
    print(f"تعداد نمونه‌های انتخاب‌شده: {len(df_sample)}")

    # تولید متن برای هر نمونه
    results = []
    for i, row in tqdm(df_sample.iterrows(), total=len(df_sample), desc="تولید متن"):
        prompt = build_prompt(row['question'], row['answer'], row['label'])
        attack_text = generate_text(prompt)
        
        if attack_text and len(attack_text) > 20:
            results.append({
                'attack_text': attack_text,
                'label': row['label'],
                'source_question': row['question'],
            })

    # ذخیره خروجی
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')

    print(f"\n✅ تعداد متن‌های تولیدشده: {len(results)}")
    print(f"✅ ذخیره شد در: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()