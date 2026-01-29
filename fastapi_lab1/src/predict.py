import joblib 


def load_model(model_path='../model/penguin_model.pkl'):
    model = joblib.load(model_path)
    return model

def predict_species(features):
    model = load_model()
    predictions = model.predict(features)
    return predictions