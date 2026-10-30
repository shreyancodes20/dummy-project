from pydantic import BaseModel, Field
from typing import Literal, Annotated



class user_input(BaseModel):
    study_hours:Annotated[float, Field(gt=0, lt=24, description="Number of hours studied per day")]
    attendance:Annotated[float, Field(gt=0, lt=100, description="Attendance percentage")]
    previous_score:Annotated[float, Field(gt=0, lt=100, description="Previous exam score percentage")]
    study_mode:Annotated[Literal["self", "coaching","group"], Field(description="Mode of study: online or offline")]