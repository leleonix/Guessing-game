# Guessing-game
# Gra w Zgadywanie Liczb z FastAPI i PostgreSQL

## Wymagania

- Python 3.8+
- PostgreSQL

## Instalacja

1. Sklonuj repozytorium:

    ```bash
    git clone 
    cd guessing_game
    ```

2. Utwórz i aktywuj wirtualne środowisko:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Zainstaluj wymagane biblioteki:

    ```bash
    pip install -r requirements.txt
    ```

4. Skonfiguruj bazę danych PostgreSQL:

    - Utwórz użytkownika i bazę danych:

        ```bash
        sudo -u postgres psql
        ```

        ```sql
        CREATE USER game_user WITH PASSWORD 'game_password';
        CREATE DATABASE guessing_game_db;
        GRANT ALL PRIVILEGES ON DATABASE guessing_game_db TO game_user;
        \q
        ```

5. Zaktualizuj `database.py` (jeśli nie zostało to już zrobione) i uruchom aplikację:

    ```bash
    uvicorn main:app --reload
    ```

6. Otwórz przeglądarkę i przejdź do `http://127.0.0.1:8000`.

## Użycie

- Endpoint do dodawania zgadywania: `POST /guess/`
- Endpoint do pobierania wyników: `GET /results/`
