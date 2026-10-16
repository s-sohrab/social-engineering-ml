# 🛡️ Social Engineering Attack Classification in Persian Text

**Automatic multi-class classification of social engineering attacks in Persian (Farsi) text using classical machine learning.**

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-Research-green.svg)](#-license)
[![Dataset](https://img.shields.io/badge/Dataset-HuggingFace-yellow.svg)](https://huggingface.co/datasets/smd20/social-engineering-qa-persian)

> **Persian version below** | **نسخه فارسی در ادامه**

---

## 📖 Overview

This project defines a novel machine learning task on the public dataset [`smd20/social-engineering-qa-persian`](https://huggingface.co/datasets/smd20/social-engineering-qa-persian). Using a transparent keyword-based weak labeling approach, 658 samples were extracted across 6 main social engineering attack classes.

Four classical machine learning models (Naive Bayes, Logistic Regression, Linear SVM, Random Forest) were trained within a standard TF-IDF-based pipeline, with full adherence to data leakage prevention principles.

**Key Result:** Linear SVM achieved **Macro-F1 = 0.9237** and **Accuracy = 0.93** on the held-out test set.

---

## 🎯 Target Classes

| Class | Description | Samples |
|---|---|---|
| `phishing` | Email phishing | 320 |
| `impersonation` | Identity impersonation | 177 |
| `vishing` | Voice phishing | 65 |
| `baiting` | Physical baiting | 34 |
| `smishing` | SMS phishing | 33 |
| `tech_support` | Tech support scam | 29 |
| **Total** | — | **658** |

---

## 📂 Project Structure

```
social-engineering-ml/
├── code/                       # Python scripts
│   ├── download_data.py        # Dataset download
│   ├── label_and_split.py      # Weak labeling & split
│   ├── train_models.py         # Train 4 models
│   ├── error_analysis.py       # Error analysis
│   └── plot_results.py         # Generate plots
├── data/                       # Original dataset
├── results/                    # Outputs (CSV, PNG)
├── dataset_labeled.jsonl       # Labeled dataset
├── requirements.txt            # Dependencies
└── README.md
```

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/social-engineering-ml.git
cd social-engineering-ml
```

### 2. Create virtual environment

```bash
python -m venv .venv

# Windows:
.venv\Scripts\activate

# macOS/Linux:
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the pipeline

```bash
python code/download_data.py       # Download dataset
python code/label_and_split.py     # Label & split
python code/train_models.py        # Train models
python code/error_analysis.py      # Error analysis
python code/plot_results.py        # Generate plots
```

---

## 📊 Results

### Cross-Validation Performance (5-Fold Stratified)

| Model | Mean Macro-F1 | Std |
|---|---|---|
| Naive Bayes | 0.2288 | ±0.0320 |
| Logistic Regression | 0.8466 | ±0.0436 |
| **Linear SVM** | **0.8708** | **±0.0311** |
| Random Forest | 0.8611 | ±0.0747 |

### Final Performance of Linear SVM (Test Set)

| Metric | Value |
|---|---|
| Accuracy | **0.93** |
| Macro-F1 | **0.9237** |
| Weighted-F1 | 0.93 |

### Error Analysis

All 8 misclassified samples (6.1%) occurred between conceptually overlapping classes (`vishing` ↔ `impersonation`, `tech_support` ↔ `impersonation`), demonstrating **semantic learning** rather than pattern memorization.

---

## 🔬 Key Contributions

1. **First Persian benchmark** for automatic classification of social engineering attacks.
2. **Transparent weak labeling** methodology based on linguistic keywords.
3. **Meaningful error analysis** showing that all errors occur at conceptual boundaries.
4. **Model interpretability** via extraction of top-10 keywords per class.

---

## 🛠️ Technologies

- **Language:** Python 3.10
- **Data processing:** pandas, numpy
- **Machine Learning:** scikit-learn
- **Dataset:** Hugging Face `datasets`
- **Visualization:** matplotlib, seaborn

---

## 📜 License

This project is released for **research and educational** purposes. The underlying reference books remain the intellectual property of their respective authors and publishers.

---

## 👤 Author

**[samad sohrab]**
---

## 📚 Citation

If you use this project in your research, please cite:

```bibtex
@misc{your-project-2026,
  title  = {Social Engineering Attack Classification in Persian Text},
  author = {[samad sohrab]},
  year   = {2026},
  url    = {https://github.com/YOUR-USERNAME/social-engineering-ml}
}
```

---

## 🙏 Acknowledgments

We thank the creators of the [Social Engineering Q&A Dataset (Persian)](https://huggingface.co/datasets/smd20/social-engineering-qa-persian) for making their dataset publicly available.

---
---

# 🇮🇷 نسخه فارسی

## 🛡️ تشخیص خودکار نوع حملات مهندسی اجتماعی در متون فارسی

**طبقه‌بندی چندکلاسه‌ی خودکار حملات مهندسی اجتماعی در متون فارسی با استفاده از یادگیری ماشین کلاسیک.**

---

## 📖 خلاصه پروژه

این پروژه یک وظیفه‌ی یادگیری ماشین جدید روی دیتاست عمومی [`smd20/social-engineering-qa-persian`](https://huggingface.co/datasets/smd20/social-engineering-qa-persian) تعریف می‌کند. با اعمال روش برچسب‌گذاری ضعیف مبتنی بر کلیدواژه، ۶۵۸ نمونه در قالب ۶ کلاس اصلی حمله مهندسی اجتماعی استخراج شد.

چهار مدل یادگیری ماشین کلاسیک (Naive Bayes، Logistic Regression، Linear SVM، Random Forest) در چارچوب یک خط لوله استاندارد مبتنی بر TF-IDF و با رعایت کامل اصول جلوگیری از نشت داده آموزش داده شدند.

**نتیجه‌ی کلیدی:** مدل Linear SVM با **Macro-F1 = 0.9237** و **Accuracy = 0.93** روی مجموعه تست دست‌نخورده بهترین عملکرد را نشان داد.

---

## 🎯 کلاس‌های هدف

| کلاس | توضیح | تعداد نمونه |
|---|---|---|
| `phishing` | فیشینگ ایمیلی | ۳۲۰ |
| `impersonation` | جعل هویت | ۱۷۷ |
| `vishing` | فیشینگ صوتی | ۶۵ |
| `baiting` | طعمه‌گذاری فیزیکی | ۳۴ |
| `smishing` | فیشینگ پیامکی | ۳۳ |
| `tech_support` | کلاهبرداری پشتیبانی فنی | ۲۹ |
| **جمع** | — | **۶۵۸** |

---

## 🚀 نحوه اجرا (فارسی)

### ۱. کلون کردن مخزن

```bash
git clone https://github.com/YOUR-USERNAME/social-engineering-ml.git
cd social-engineering-ml
```

### ۲. ساخت محیط مجازی

```bash
python -m venv .venv

# ویندوز:
.venv\Scripts\activate

# مک / لینوکس:
source .venv/bin/activate
```

### ۳. نصب پکیج‌ها

```bash
pip install -r requirements.txt
```

### ۴. اجرای پروژه

```bash
python code/download_data.py       # دانلود دیتاست
python code/label_and_split.py     # برچسب‌گذاری و تقسیم
python code/train_models.py        # آموزش مدل‌ها
python code/error_analysis.py      # تحلیل خطا
python code/plot_results.py        # نمودارها
```

---

## 📊 نتایج کلیدی

### عملکرد Cross-Validation (۵-Fold Stratified)

| مدل | میانگین Macro-F1 | انحراف معیار |
|---|---|---|
| Naive Bayes | ۰.۲۲۸۸ | ±۰.۰۳۲۰ |
| Logistic Regression | ۰.۸۴۶۶ | ±۰.۰۴۳۶ |
| **Linear SVM** | **۰.۸۷۰۸** | **±۰.۰۳۱۱** |
| Random Forest | ۰.۸۶۱۱ | ±۰.۰۷۴۷ |

### عملکرد نهایی Linear SVM روی تست

| معیار | مقدار |
|---|---|
| Accuracy | **۰.۹۳** |
| Macro-F1 | **۰.۹۲۳۷** |
| Weighted-F1 | ۰.۹۳ |

---

## 🔬 نوآوری‌های پروژه

۱. **اولین benchmark فارسی** برای تشخیص خودکار نوع حملات مهندسی اجتماعی
۲. **روش برچسب‌گذاری ضعیف** شفاف و قابل بازتولید
۳. **تحلیل خطای معنادار** — تمام خطاها در مرزهای کلاس‌های هم‌پوشان مفهومی رخ داده‌اند
۴. **تفسیرپذیری مدل** — استخراج ۱۰ کلمه‌ی کلیدی مؤثر در تصمیم‌گیری

---

## 📜 لایسنس

این پروژه برای اهداف **پژوهشی و آموزشی** منتشر شده است. حقوق معنوی کتاب‌های مرجع اصلی، متعلق به نویسندگان و ناشران آن‌هاست.

---

## 👤 نویسنده

**[صمد سهراب]**
---

## 🙏 تقدیر

<<<<<<< HEAD
از سازندگان دیتاست [Social Engineering Q&A Dataset (Persian)](https://huggingface.co/datasets/smd20/social-engineering-qa-persian) که دیتاست خود را به‌صورت عمومی منتشر کردند، صمیمانه سپاسگزاریم.
=======
از سازندگان دیتاست [Social Engineering Q&A Dataset (Persian)](https://huggingface.co/datasets/smd20/social-engineering-qa-persian) که دیتاست خود را به‌صورت عمومی منتشر کردند، صمیمانه سپاسگزاریم
>>>>>>> 6023d14 (Update .gitignore)
