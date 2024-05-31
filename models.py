from sqlalchemy import Column, Integer, Boolean
from database import Base

class Guess(Base):
    __tablename__ = "guesses"

    id = Column(Integer, primary_key=True, index=True)
    number_to_guess = Column(Integer)
    correct = Column(Boolean, default=False)
    attempts = Column(Integer)
