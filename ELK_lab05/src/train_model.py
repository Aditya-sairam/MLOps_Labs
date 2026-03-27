from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def train_wine_model():
    # Load data
    wine = load_wine()
    X_train, X_test, y_train, y_test = train_test_split(
        wine.data, wine.target, test_size=0.2, random_state=42
    )
    
    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    # Create model directory relative to this file
    model_dir = os.path.join(os.path.dirname(__file__), '..', 'model')
    os.makedirs(model_dir, exist_ok=True)
    # Save model
    joblib.dump(model, os.path.join(model_dir, 'wine_model.pkl'))
    print(f"Model trained! Accuracy: {model.score(X_test, y_test):.2f}")
    
    # Save feature names and target names for later
    joblib.dump(wine.feature_names, os.path.join(model_dir,'../model/feature_names.pkl'))
    joblib.dump(wine.target_names, os.path.join(model_dir,'../model/target_names.pkl'))

if __name__ == "__main__":
    train_wine_model()