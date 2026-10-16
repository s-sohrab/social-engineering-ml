import os
import shutil

# ساخت پوشه تحویل
delivery_dir = "delivery"
os.makedirs(f"{delivery_dir}/notebook", exist_ok=True)
os.makedirs(f"{delivery_dir}/code", exist_ok=True)
os.makedirs(f"{delivery_dir}/data", exist_ok=True)
os.makedirs(f"{delivery_dir}/results", exist_ok=True)

# فایل‌های کد
code_files = [
    "download_data.py",
    "check_data.py",
    "keyword_check.py",
    "label_and_split.py",
    "train_models.py",
    "error_analysis.py",
    "plot_results.py",
    "cv_details.py",
    "extract_errors.py",
    "export_top_words.py",
]

for f in code_files:
    if os.path.exists(f):
        shutil.copy(f, f"{delivery_dir}/code/{f}")
        print(f"✅ کپی شد: {f}")

# فایل‌های داده
if os.path.exists("dataset_labeled.jsonl"):
    shutil.copy("dataset_labeled.jsonl", f"{delivery_dir}/data/")
    print("✅ کپی شد: dataset_labeled.jsonl")

# فایل‌های خروجی
result_files = [
    "cv_results.csv",
    "cv_details_appendix.csv",
    "top10_words_per_class.csv",
    "misclassified_samples.csv",
    "confusion_matrix.png",
    "plot_class_distribution.png",
    "plot_models_comparison.png",
    "plot_top_words.png",
]

for f in result_files:
    if os.path.exists(f):
        shutil.copy(f, f"{delivery_dir}/results/{f}")
        print(f"✅ کپی شد: {f}")

# فایل‌های پیکربندی
for f in ["README.md", "requirements.txt"]:
    if os.path.exists(f):
        shutil.copy(f, f"{delivery_dir}/")

print("\n✅ پوشه تحویل آماده است: ./delivery")