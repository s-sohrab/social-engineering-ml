import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.metrics import confusion_matrix, f1_score

# تنظیم فونت فارسی برای matplotlib
plt.rcParams['font.family'] = 'Vazir'
plt.rcParams['axes.unicode_minus'] = False

# =====================================================
# بارگذاری داده
# =====================================================
df = pd.read_json("dataset_labeled.jsonl", lines=True)
X, y = df['text'], df['label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# =====================================================
# نمودار ۱: توزیع کلاس‌ها
# =====================================================
print("در حال ساخت نمودار ۱: توزیع کلاس‌ها...")

label_counts = df['label'].value_counts()

plt.figure(figsize=(10, 6))
colors = sns.color_palette("viridis", len(label_counts))
bars = plt.bar(range(len(label_counts)), label_counts.values, color=colors)

plt.xticks(range(len(label_counts)), label_counts.index, rotation=45, ha='right')
plt.xlabel('نوع حمله مهندسی اجتماعی', fontsize=12)
plt.ylabel('تعداد نمونه', fontsize=12)
plt.title('توزیع کلاس‌ها در دیتاست برچسب‌خورده', fontsize=14, fontweight='bold')

# افزودن مقادیر روی میله‌ها
for bar, count in zip(bars, label_counts.values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 3,
             str(count), ha='center', fontsize=10, fontweight='bold')

plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('plot_class_distribution.png', dpi=200, bbox_inches='tight')
plt.close()
print("✅ ذخیره شد: plot_class_distribution.png")


# =====================================================
# نمودار ۲: مقایسه ۴ مدل (Cross-Validation)
# =====================================================
print("\nدر حال آموزش و ارزیابی ۴ مدل...")

models = {
    "Naive Bayes":    MultinomialNB(),
    "Logistic Reg":   LogisticRegression(max_iter=1000, class_weight='balanced'),
    "Linear SVM":     LinearSVC(class_weight='balanced', max_iter=2000),
    "Random Forest":  RandomForestClassifier(n_estimators=200, class_weight='balanced', random_state=42),
}

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
results = {}

for name, clf in models.items():
    pipe = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=2, max_df=0.9)),
        ("clf", clf)
    ])
    scores = cross_val_score(pipe, X_train, y_train, cv=cv, scoring="f1_macro")
    results[name] = scores
    print(f"  {name:<15} Macro-F1 = {scores.mean():.4f} ± {scores.std():.4f}")

# ذخیره نتایج CV در CSV
cv_df = pd.DataFrame({
    'Model': list(results.keys()),
    'Mean_MacroF1': [results[k].mean() for k in results],
    'Std_MacroF1': [results[k].std() for k in results],
})
cv_df.to_csv('cv_results.csv', index=False, encoding='utf-8-sig')
print("✅ ذخیره شد: cv_results.csv")

# نمودار مقایسه مدل‌ها (Box plot)
plt.figure(figsize=(10, 6))
data_for_plot = [results[k] for k in results.keys()]
import matplotlib
try:
    # نسخه جدید
    bp = plt.boxplot(data_for_plot, tick_labels=list(results.keys()),
                      patch_artist=True, widths=0.6)
except TypeError:
    # نسخه قدیمی
    bp = plt.boxplot(data_for_plot, labels=list(results.keys()),
                      patch_artist=True, widths=0.6)

colors = sns.color_palette("Set2", len(results))
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.8)

plt.ylabel('Macro-F1 (5-Fold CV)', fontsize=12)
plt.xlabel('مدل', fontsize=12)
plt.title('مقایسه عملکرد ۴ مدل با Cross-Validation', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('plot_models_comparison.png', dpi=200, bbox_inches='tight')
plt.close()
print("✅ ذخیره شد: plot_models_comparison.png")


# =====================================================
# نمودار ۳: Top-Words هر کلاس (از بهترین مدل: SVM)
# =====================================================
print("\nدر حال استخراج Top-Words هر کلاس (SVM)...")

best_pipe = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=2, max_df=0.9)),
    ("clf", LinearSVC(class_weight='balanced', max_iter=2000))
])
best_pipe.fit(X_train, y_train)

vectorizer = best_pipe.named_steps['tfidf']
clf = best_pipe.named_steps['clf']
feature_names = vectorizer.get_feature_names_out()
classes = clf.classes_

# ساخت نمودار شبکه‌ای 2x3
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
axes = axes.flatten()

top_words_dict = {}
for i, label in enumerate(classes):
    coefs = clf.coef_[i]
    top_idx = np.argsort(coefs)[-10:][::-1]
    top_words = [feature_names[j] for j in top_idx]
    top_scores = [coefs[j] for j in top_idx]
    top_words_dict[label] = top_words

    ax = axes[i]
    colors = sns.color_palette("rocket", len(top_words))
    ax.barh(range(len(top_words)), top_scores[::-1], color=colors)
    ax.set_yticks(range(len(top_words)))
    ax.set_yticklabels(top_words[::-1], fontsize=9)
    ax.set_xlabel('وزن در مدل', fontsize=9)
    ax.set_title(f'کلاس: {label}', fontsize=11, fontweight='bold')
    ax.grid(axis='x', alpha=0.3)

plt.suptitle('۱۰ کلمه‌ی مهم هر کلاس در مدل Linear SVM',
             fontsize=14, fontweight='bold', y=1.00)
plt.tight_layout()
plt.savefig('plot_top_words.png', dpi=200, bbox_inches='tight')
plt.close()
print("✅ ذخیره شد: plot_top_words.png")

# ذخیره Top-Words در CSV
top_words_df = pd.DataFrame({
    f"top{i+1}": [top_words_dict[l][i] for l in classes]
    for i in range(10)
})
top_words_df.index = classes
top_words_df.to_csv('top_words_per_class.csv', encoding='utf-8-sig')
print("✅ ذخیره شد: top_words_per_class.csv")


# =====================================================
# گزارش نهایی
# =====================================================
print("\n" + "=" * 60)
print("خلاصه فایل‌های ساخته‌شده:")
print("=" * 60)
print("  📊 plot_class_distribution.png    ← توزیع کلاس‌ها")
print("  📊 plot_models_comparison.png     ← مقایسه ۴ مدل")
print("  📊 plot_top_words.png             ← Top-words هر کلاس")
print("  📄 cv_results.csv                 ← نتایج CV")
print("  📄 top_words_per_class.csv        ← کلمات مهم")
print("\n✅ تمام!")