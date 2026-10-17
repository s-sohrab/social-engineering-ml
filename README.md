# 🛡️ Social Engineering Attack Classification in Persian Text

**Automatic multi-class classification of social engineering attacks in Persian (Farsi) text using classical machine learning.**

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📖 Overview

This project is organized in **two phases**:

**Phase 1: Classification of Social Engineering Q&A**
- **Dataset:** `smd20/social-engineering-qa-persian` (3,330 Persian Q&A pairs)
- **Task:** Classify the type of social engineering attack from question-answer text
- **Result:** **Linear SVM** with **Macro-F1 = 0.9237** and **Accuracy = 0.93**

**Phase 2: Classification of Generated Attack Texts**
- **Dataset:** 246 real attack texts generated from Phase 1 data using **Qwen 2.5 (7B)** via Ollama
- **Task:** Classify the type of social engineering attack from realistic attack texts
- **Result:** **Linear SVM** with **Macro-F1 = 0.6891** and **Accuracy = 0.68**

**Key Finding:** Phase 2 is significantly harder than Phase 1 because real attack texts are more diverse and realistic than Q&A pairs.

---

## 📂 Project Structure

The repository is organized as follows:

- `phase1/` – Phase 1: Q&A classification (code, data, results)
- `phase2/` – Phase 2: Attack text classification (code, data, results)
- `README.md` – This file
- `requirements.txt` – Python dependencies

---

## 🎯 Target Classes

| Class | Description | Phase 1 Samples | Phase 2 Samples |
|---|---|---|---|
| `phishing` | Email phishing | 320 | 50 |
| `impersonation` | Identity impersonation | 177 | 50 |
| `vishing` | Voice phishing | 65 | 50 |
| `baiting` | Physical baiting | 34 | 34 |
| `smishing` | SMS phishing | 33 | 33 |
| `tech_support` | Tech support scam | 29 | 29 |
| **Total** | — | **658** | **246** |

---

## 🚀 Quick Start

To run the project, follow these steps:

1. Clone the repository using `git clone https://github.com/s-sohrab/social-engineering-ml.git` and navigate into it.
2. Create and activate a virtual environment using `python -m venv .venv` and then `.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (macOS/Linux).
3. Install dependencies with `pip install -r requirements.txt`.
4. For Phase 1, run the scripts in `phase1/code/` in order: `label_and_split.py`, `train_models.py`, and `error_analysis.py`.
5. For Phase 2, first ensure Ollama is installed and the model is pulled (`ollama pull qwen2.5:7b`), then run `generate_attack_texts.py`, `train_models_phase2.py`, and `compare_phases.py` from `phase2/code/`.

---

## 📊 Results

### Phase 1: Q&A Classification (5-Fold CV)

| Model | Mean Macro-F1 | Std |
|---|---|---|
| Naive Bayes | 0.2288 | ±0.0320 |
| Logistic Regression | 0.8466 | ±0.0436 |
| **Linear SVM** | **0.8708** | **±0.0311** |
| Random Forest | 0.8611 | ±0.0747 |

### Phase 2: Attack Text Classification (5-Fold CV)

| Model | Mean Macro-F1 | Std |
|---|---|---|
| Naive Bayes | 0.3791 | ±0.0598 |
| Logistic Regression | 0.6173 | ±0.0665 |
| **Linear SVM** | **0.6272** | **±0.0740** |
| Random Forest | 0.5550 | ±0.0526 |

### Final Test Performance (Linear SVM)

| Metric | Phase 1 | Phase 2 |
|---|---|---|
| Accuracy | **0.93** | **0.68** |
| Macro-F1 | **0.9237** | **0.6891** |

---

## 🔬 Key Contributions

1. **First Persian benchmark** for automatic classification of social engineering attacks.
2. **Transparent weak labeling** methodology based on linguistic keywords.
3. **Meaningful error analysis** showing that all errors occur at conceptual boundaries.
4. **Two-phase evaluation:** comparing Q&A classification vs. real attack text classification.
5. **Model interpretability** via extraction of top-10 keywords per class.

---

## 🛠️ Technologies

- **Language:** Python 3.10
- **Data processing:** pandas, numpy
- **Machine Learning:** scikit-learn
- **LLM for data generation:** Qwen 2.5 (7B) via Ollama
- **Visualization:** matplotlib, seaborn

---

## 📜 License

This project is released for **research and educational** purposes under the **MIT License**.

---

## 👤 Author

**Samad Sohrab**

---

## 📚 Citation

If you use this project in your research, please cite it as follows:

```bibtex
@misc{sohrab2026social,
  title  = {Social Engineering Attack Classification in Persian Text},
  author = {Sohrab, Samad},
  year   = {2026},
  url    = {https://github.com/s-sohrab/social-engineering-ml}
}


🇮🇷 نسخه فارسی
🛡️ تشخیص خودکار نوع حملات مهندسی اجتماعی در متون فارسی
طبقه‌بندی چندکلاسه‌ی خودکار حملات مهندسی اجتماعی در متون فارسی با استفاده از یادگیری ماشین کلاسیک.

📖 خلاصه پروژه
این پروژه در دو فاز سازمان‌دهی شده است:

فاز اول： طبقه‌بندی پرسش‌وپاسخ‌های مهندسی اجتماعی

دیتاست： smd20/social-engineering-qa-persian (۳,۳۳۰ جفت پرسش-پاسخ فارسی)

وظیفه： تشخیص نوع حمله از روی متن پرسش‌وپاسخ

نتیجه： Linear SVM با Macro-F1 = 0.9237 و Accuracy = 0.93

فاز دوم： طبقه‌بندی متن‌های واقعی حمله

دیتاست： ۲۴۶ متن واقعی حمله که با Qwen 2.5 (7B) و از طریق Ollama از داده‌های فاز اول تولید شده‌اند

وظیفه： تشخیص نوع حمله از روی متن واقعی

نتیجه： Linear SVM با Macro-F1 = 0.6891 و Accuracy = 0.68

یافته کلیدی： فاز دوم به‌مراتب سخت‌تر از فاز اول است، چون متن‌های واقعی حمله تنوع و پیچیدگی بیشتری نسبت به پرسش‌وپاسخ دارند.

🎯 کلاس‌های هدف
کلاس	توضیح	تعداد (فاز اول)	تعداد (فاز دوم)
phishing	فیشینگ ایمیلی	۳۲۰	۵۰
impersonation	جعل هویت	۱۷۷	۵۰
vishing	فیشینگ صوتی	۶۵	۵۰
baiting	طعمه‌گذاری فیزیکی	۳۴	۳۴
smishing	فیشینگ پیامکی	۳۳	۳۳
tech_support	کلاهبرداری پشتیبانی فنی	۲۹	۲۹
جمع	—	۶۵۸	۲۴۶
🚀 نحوه اجرا
برای اجرای پروژه، مراحل زیر را دنبال کنید:

۱. مخزن را با دستور git clone https://github.com/s-sohrab/social-engineering-ml.git کلون کرده و وارد پوشه آن شوید.
۲. یک محیط مجازی با دستور python -m venv .venv بسازید و آن را فعال کنید (در ویندوز： .venv\Scripts\activate و در مک/لینوکس： source .venv/bin/activate).
۳. وابستگی‌ها را با دستور pip install -r requirements.txt نصب کنید.
۴. برای فاز اول، اسکریپت‌های پوشه phase1/code/ را به‌ترتیب اجرا کنید： label_and_split.py، train_models.py و error_analysis.py.
۵. برای فاز دوم، ابتدا مطمئن شوید Ollama نصب و مدل دانلود شده است (ollama pull qwen2.5:7b)، سپس اسکریپت‌های generate_attack_texts.py، train_models_phase2.py و compare_phases.py را از پوشه phase2/code/ اجرا کنید.

📊 نتایج
فاز اول： طبقه‌بندی پرسش‌وپاسخ (۵-Fold CV)
مدل	میانگین Macro-F1	انحراف معیار
Naive Bayes	۰.۲۲۸۸	±۰.۰۳۲۰
Logistic Regression	۰.۸۴۶۶	±۰.۰۴۳۶
Linear SVM	۰.۸۷۰۸	±۰.۰۳۱۱
Random Forest	۰.۸۶۱۱	±۰.۰۷۴۷
فاز دوم： طبقه‌بندی متن حمله (۵-Fold CV)
مدل	میانگین Macro-F1	انحراف معیار
Naive Bayes	۰.۳۷۹۱	±۰.۰۵۹۸
Logistic Regression	۰.۶۱۷۳	±۰.۰۶۶۵
Linear SVM	۰.۶۲۷۲	±۰.۰۷۴۰
Random Forest	۰.۵۵۵۰	±۰.۰۵۲۶
عملکرد نهایی Linear SVM روی تست
معیار	فاز اول	فاز دوم
Accuracy	۰.۹۳	۰.۶۸
Macro-F1	۰.۹۲۳۷	۰.۶۸۹۱
🔬 نوآوری‌ها
۱. اولین benchmark فارسی برای تشخیص خودکار نوع حملات مهندسی اجتماعی
۲. روش برچسب‌گذاری ضعیف شفاف و قابل بازتولید
۳. تحلیل خطای معنادار — تمام خطاها در مرزهای کلاس‌های هم‌پوشان مفهومی رخ داده‌اند
۴. ارزیابی دوفازی： مقایسه طبقه‌بندی پرسش‌وپاسخ با طبقه‌بندی متن واقعی حمله
۵. تفسیرپذیری مدل — استخراج ۱۰ کلمه‌ی کلیدی مؤثر در تصمیم‌گیری

🛠️ فناوری‌ها
زبان： Python 3.10

پردازش داده： pandas, numpy

یادگیری ماشین： scikit-learn

مدل زبانی برای تولید داده： Qwen 2.5 (7B) از طریق Ollama

مصورسازی： matplotlib, seaborn

📜 لایسنس
این پروژه برای اهداف پژوهشی و آموزشی تحت لایسنس MIT منتشر شده است.

👤 نویسنده
صمد سهراب
