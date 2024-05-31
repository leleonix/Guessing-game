from pydantic import BaseModel, ConfigDict

class GuessBase(BaseModel):
    number_to_guess: int
    correct: bool
    attempts: int

class GuessCreate(BaseModel):
    number: int

class GuessResult(GuessBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
