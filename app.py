from fastapi import FastAPI
from fastapi.responses import JSONResponse


from schema.user_response import PredictionResponse
from model.prediction_result import predict_output
from schema.user_input import user_input

app = FastAPI()



@app.post("/predict", response_model=PredictionResponse)
def predict(data: user_input):
    input_dict = {
        "study_hours": data.study_hours,
        "attendance": data.attendance,
        "previous_score": data.previous_score,
        "study_mode": data.study_mode,
    }

    try:
        prediction_result = predict_output(input_dict)
        return JSONResponse(content=prediction_result, status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)