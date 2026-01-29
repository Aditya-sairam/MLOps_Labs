from sklearn.ensemble import RandomForestClassifier
from data import load_data, clean_data, feature_engineering, split_data
from sklearn.metrics import accuracy_score, classification_report
import joblib

def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def predict(model, X):
    predictions = model.predict(X)
    return predictions

def evaluate_model(model, X_test, y_test):
    """Evaluate the model on test data"""
    
    # TODO: Make predictions on X_test
    y_pred = model.predict(X_test)
    
    # TODO: Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Accuracy: {accuracy:.2f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    return accuracy

def save_model(model, filepath='../model/penguin_model.pkl'):
    joblib.dump(model, filepath)
