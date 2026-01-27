import joblib
import os
from pathlib import Path

# Get the absolute path to the model file
model_path = Path(__file__).parent.parent / "model" / "disease_model.pkl"

try:
    model = joblib.load(model_path)
    print(f"✓ Model loaded successfully from {model_path}")
except Exception as e:
    print(f"✗ Error loading model from {model_path}: {e}")
    model = None
