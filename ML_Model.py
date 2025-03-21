import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import seaborn as sns


df = sns.load_dataset('titanic')


df.dropna(subset=['age', 'fare', 'sex', 'class', 'survived'], inplace=True)
df['sex'] = df['sex'].map({'male': 0, 'female': 1})
df['class'] = df['class'].map({'First': 1, 'Second': 2, 'Third': 3})


X = df[['age', 'fare', 'sex', 'class']]
y = df['survived']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LogisticRegression()
model.fit(X_train, y_train)

s
y_pred = model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy * 100:.2f}%')
