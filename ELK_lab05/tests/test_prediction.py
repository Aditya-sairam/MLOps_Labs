import requests
import random
import time

url = "http://localhost:8000/predict"

# Sample wine feature ranges (based on wine dataset)
wine_samples = [
    # Class 0 - typically higher alcohol, proline
    {"alcohol": 13.5, "malic_acid": 2.3, "ash": 2.4, "alcalinity_of_ash": 20.0, 
     "magnesium": 100.0, "total_phenols": 2.8, "flavanoids": 3.0, 
     "nonflavanoid_phenols": 0.3, "proanthocyanins": 1.9, "color_intensity": 5.5,
     "hue": 1.1, "od280_od315_of_diluted_wines": 3.2, "proline": 1100.0},
    
    # Class 1 - medium values
    {"alcohol": 12.5, "malic_acid": 2.0, "ash": 2.2, "alcalinity_of_ash": 19.0,
     "magnesium": 95.0, "total_phenols": 2.3, "flavanoids": 2.0,
     "nonflavanoid_phenols": 0.35, "proanthocyanins": 1.5, "color_intensity": 4.5,
     "hue": 0.95, "od280_od315_of_diluted_wines": 2.8, "proline": 900.0},
    
    # Class 2 - lower values
    {"alcohol": 12.0, "malic_acid": 3.5, "ash": 2.6, "alcalinity_of_ash": 21.0,
     "magnesium": 85.0, "total_phenols": 1.8, "flavanoids": 1.2,
     "nonflavanoid_phenols": 0.45, "proanthocyanins": 1.0, "color_intensity": 3.5,
     "hue": 0.8, "od280_od315_of_diluted_wines": 2.2, "proline": 600.0}
]

print("Sending predictions to API...")
for i in range(20):
    # Pick a random sample and add some variation
    sample = random.choice(wine_samples).copy()
    
    # Add small random variations
    for key in sample:
        sample[key] += random.uniform(-0.5, 0.5)
    
    response = requests.post(url, json=sample)
    print(f"Prediction {i+1}: {response.json()}")
    time.sleep(0.5)  # Small delay

print("Done! Check your Kibana dashboard!")