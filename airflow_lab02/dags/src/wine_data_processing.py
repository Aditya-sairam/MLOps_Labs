from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import numpy as np
import pickle
import base64

def load_data_task(**context):
    """Load wine dataset and push to XCom"""
    print("Loading wine dataset...")
    wine = load_wine()
    
    # Create dataframe
    df = pd.DataFrame(wine.data, columns=wine.feature_names)
    df['target'] = wine.target
    
    print(f"Dataset loaded successfully!")
    print(f"Shape: {df.shape}")
    
    # Serialize and encode
    serialized_data = pickle.dumps(df)
    encoded_data = base64.b64encode(serialized_data).decode("ascii")
    
    # Push to XCom
    context['ti'].xcom_push(key='wine_data', value=encoded_data)
    context['ti'].xcom_push(key='target_names', value=wine.target_names.tolist())
    
    return {"status": "success", "shape": df.shape}

def clean_data_task(**context):
    """Clean and preprocess data"""
    print("Cleaning data...")
    
    # Pull from XCom and deserialize
    encoded_data = context['ti'].xcom_pull(key='wine_data', task_ids='load_data')
    df = pickle.loads(base64.b64decode(encoded_data))
    
    # Check for missing values
    missing = df.isnull().sum().sum()
    print(f"Missing values: {missing}")
    df.fillna(df.mean(), inplace=True)
    print("Data is now clean and ready for training.")
    # Serialize and push cleaned data
    serialized_data = pickle.dumps(df)
    encoded_data = base64.b64encode(serialized_data).decode("ascii")
    context['ti'].xcom_push(key='cleaned_data', value=encoded_data)
    
    return {"status": "cleaned"}

def train_model_task(**context):
    """Train the model"""
    print("Training model...")
    
    # Pull cleaned data from XCom
    encoded_data = context['ti'].xcom_pull(key='cleaned_data', task_ids='clean_data')
    df = pickle.loads(base64.b64decode(encoded_data))
    
    # Split features and target
    X = df.drop('target', axis=1).values
    y = df['target'].values
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Training accuracy
    train_pred = model.predict(X_train)
    train_accuracy = accuracy_score(y_train, train_pred)
    
    print(f"Training completed!")
    print(f"Training Accuracy: {train_accuracy:.2f}")
    
    # Serialize and push train/test data
    context['ti'].xcom_push(key='X_train', value=base64.b64encode(pickle.dumps(X_train)).decode("ascii"))
    context['ti'].xcom_push(key='X_test', value=base64.b64encode(pickle.dumps(X_test)).decode("ascii"))
    context['ti'].xcom_push(key='y_train', value=base64.b64encode(pickle.dumps(y_train)).decode("ascii"))
    context['ti'].xcom_push(key='y_test', value=base64.b64encode(pickle.dumps(y_test)).decode("ascii"))
    
    return {"status": "trained", "train_accuracy": train_accuracy}

def evaluate_model_task(**context):
    """Evaluate the model on test data"""
    print("Evaluating model...")
    
    # Pull data from XCom and deserialize
    X_train = pickle.loads(base64.b64decode(context['ti'].xcom_pull(key='X_train', task_ids='train_model')))
    X_test = pickle.loads(base64.b64decode(context['ti'].xcom_pull(key='X_test', task_ids='train_model')))
    y_train = pickle.loads(base64.b64decode(context['ti'].xcom_pull(key='y_train', task_ids='train_model')))
    y_test = pickle.loads(base64.b64decode(context['ti'].xcom_pull(key='y_test', task_ids='train_model')))
    target_names = context['ti'].xcom_pull(key='target_names', task_ids='load_data')
    
    # Retrain model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate on test set
    y_pred = model.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\nTest Accuracy: {test_accuracy:.2f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=target_names))
    
    return {"status": "evaluated", "test_accuracy": test_accuracy}