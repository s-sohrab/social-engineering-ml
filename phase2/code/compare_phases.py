import json
import pandas as pd

# بارگذاری نتایج دو فاز
with open("phase2/results/phase2_results.json", "r", encoding="utf-8") as f:
    phase2 = json.load(f)

# نتایج فاز اول (دستی)
phase1 = {
    "best_model": "Linear SVM",
    "test_accuracy": 0.93,
    "test_macro_f1": 0.9237,
    "n_samples": 658,
    "cv_results": {
        "Naive Bayes": {"mean": 0.2288, "std": 0.0320},
        "Logistic Regression": {"mean": 0.8466, "std": 0.0436},
        "Linear SVM": {"mean": 0.8708, "std": 0.0311},
        "Random Forest": {"mean": 0.8611, "std": 0.0747},
    }
}

# ساخت جدول مقایسه
print("=" * 70)
print("مقایسه فاز اول و فاز دوم")
print("=" * 70)

comparison = pd.DataFrame({
    "معیار": ["تعداد نمونه", "مدل برتر", "Accuracy (تست)", "Macro-F1 (تست)"],
    "فاز اول (پرسش‌وپاسخ)": [
        phase1["n_samples"],
        phase1["best_model"],
        phase1["test_accuracy"],
        phase1["test_macro_f1"]
    ],
    "فاز دوم (متن حمله)": [
        phase2["n_samples"],
        phase2["best_model"],
        phase2["test_accuracy"],
        phase2["test_macro_f1"]
    ]
})

print(comparison.to_string(index=False))

# ذخیره در CSV
comparison.to_csv("phase2/results/comparison.csv", index=False, encoding="utf-8-sig")
print("\n✅ ذخیره شد: phase2/results/comparison.csv")

# تحلیل تفاوت
print("\n" + "=" * 70)
print("تحلیل تفاوت:")
print("=" * 70)
diff_acc = phase2["test_accuracy"] - phase1["test_accuracy"]
diff_f1 = phase2["test_macro_f1"] - phase1["test_macro_f1"]
print(f"تفاوت Accuracy: {diff_acc:+.4f}")
print(f"تفاوت Macro-F1: {diff_f1:+.4f}")
print(f"\nنتیجه: فاز دوم به دلیل ماهیت سخت‌تر داده‌ها (متن واقعی حمله به‌جای پرسش‌وپاسخ) و تعداد کمتر نمونه، عملکرد پایین‌تری دارد.")
