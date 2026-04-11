from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

wine = load_wine()
X_train, X_test, y_train, y_test = train_test_split(
    wine.data, wine.target, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, 'model/wine_model.pkl')
joblib.dump(wine.target_names, 'model/target_names.pkl')
print(f"Model trained! Accuracy: {model.score(X_test, y_test):.2f}")