from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

if os.getenv("CONNECTION_STRING"):
    SQLALCHEMY_DATABASE_URL = os.getenv("CONNECTION_STRING")
else:
    SQLALCHEMY_DATABASE_URL = "postgresql://postgres:test1234@host.docker.internal:5432/fastapidb"
    
DATABASE_URL = "postgresql://game_user:password12+@localhost/guessing_game_db"

engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

