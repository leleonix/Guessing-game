from typing import Union

from fastapi import FastAPI

import models 
from database import engine

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from typing import List
import crud, schemas

from database import SessionLocal
import random

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/guess/", response_model=schemas.GuessResult)
def make_guess(guess: schemas.GuessCreate, db: Session = Depends(get_db)):
    number_to_guess = random.randint(1, 100)
    correct = guess.number == number_to_guess
    result = schemas.GuessResult(
        number_to_guess=number_to_guess,
        correct=correct,
        attempts=1
    )
    crud.create_guess(db=db, guess=result)
    return result

@app.get("/results/", response_model=List[schemas.GuessResult])
def read_results(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    results = crud.get_guesses(db, skip=skip, limit=limit)
    return results
