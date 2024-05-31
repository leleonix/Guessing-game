from sqlalchemy.sql import text
from database import engine

def test_connection():
    try:
        stmt = text("SELECT 1")
        
        with engine.connect() as conn:
            result = conn.execute(stmt)
            print("Połączenie z bazą danych działa prawidłowo")
    except Exception as e:
        print(f"Błąd połączenia z bazą danych: {e}")

if __name__ == "__main__":
    test_connection()
