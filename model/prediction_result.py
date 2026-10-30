import pickle
import pandas as pd
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
MODEL_VERSION = "1.0.0"
class_labels = model.classes_.tolist()

def predict_output(user_input:dict):
    input_df= pd.DataFrame([user_input])
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]
    confidence=max(probability)
    class_prob=dict(zip(class_labels,map(lambda p:round(p,4), probability)))

    return{"predicted_category": str(prediction), "probability": class_prob}