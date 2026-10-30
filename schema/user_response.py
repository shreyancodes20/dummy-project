from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category: str = Field(
        ...,
        description="The predicted result",
        example="Pass"
    )
    
    class_probabilities: Dict[str, float] = Field(
        ...,
        description="Probability distribution across all possible classes",
        example={"Pass": 0.01, "Fail": 0.15}
    )