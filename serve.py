import json
import joblib
import numpy as np

def model_fn(model_dir):
    model = joblib.load(f"{model_dir}/model.joblib")
    return model

def input_fn(request_body, content_type):
    if content_type == "application/json":
        data = json.loads(request_body)
        return np.array(data["input"]).reshape(1, -1)
    else:
        raise ValueError("Unsupported content type")

def predict_fn(input_data, model):
    prediction = model.predict(input_data)
    return prediction.tolist()

def output_fn(prediction, content_type):
    return json.dumps({"prediction": prediction}), content_type
