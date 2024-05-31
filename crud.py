from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import select
import schemas, models

def get_guesses(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Guess).offset(skip).limit(limit).all()

def create_guess(db: Session, guess: schemas.GuessResult):
    db_guess = models.Guess(**guess.dict())
    db.add(db_guess)
    db.commit()
    db.refresh(db_guess)
    return db_guess

