import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score

# بارگذاری داده
df = pd.read_json("dataset_labeled.jsonl", lines=True)
X, y = df['text'], df['label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

models = {
    "Naive Bayes":         MultinomialNB(),
    "Logistic Regression": LogisticRegression(max_iter=1000, class_weight='balanced'),
    "Linear SVM":          LinearSVC(class_weight='balanced', max_iter=2000),
    "Random Forest":       RandomForestClassifier(n_estimators=200, class_weight='balanced', random_state=42),
}

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# استخراج امتیاز هر fold
results_dict = {"Fold": [1, 2, 3, 4, 5]}
for name, clf in models.items():
    pipe = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=2, max_df=0.9)),
        ("clf", clf)
    ])
    scores = cross_val_score(pipe, X_train, y_train, cv=cv, scoring="f1_macro")
    results_dict[name] = scores.round(4)

# ساخت DataFrame
df_cv = pd.DataFrame(results_dict)

# افزودن Mean و Std
df_cv.loc['Mean'] = df_cv.iloc[:, 1:].mean().round(4)
df_cv.loc['Std'] = df_cv.iloc[:5, 1:].std().round(4)

print(df_cv.to_string(index=False))

# ذخیره در CSV
df_cv.to_csv('cv_details_appendix.csv', index=False, encoding='utf-8-sig')
print("\n✅ ذخیره شد: cv_details_appendix.csv")