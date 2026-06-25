from contextlib import asynccontextmanager   # инструмент для lifespan
from fastapi import FastAPI
import os
import time          # для пауз между попытками
import psycopg

host = os.getenv("POSTGRES_HOST")        # "db" — пришло из .env через compose
password = os.getenv("POSTGRES_PASSWORD")  # пароль — оттуда же

def wait_for_db(retries=10, delay=2):
    for attempt in range(1, retries + 1):          # попытки 1..10
        try:
            with psycopg.connect(                  # пробуем открыть соединение
                host=host,
                dbname="postgres",
                user="postgres",
                password=password,
            ) as conn:
                with conn.cursor() as cur:         # курсор = «рука», которой шлём запрос
                    cur.execute("SELECT 1")        # дешёвый запрос-пинг
                    cur.fetchone()                 # забрать ответ
            print(f"DB connected on attempt {attempt}")
            return                                 # успех → выходим из функции
        except psycopg.OperationalError:           # база ещё не готова
            print(f"Attempt {attempt}/{retries}: DB not ready, retry in {delay}s")
            time.sleep(delay)                      # ждём и пробуем снова
    raise RuntimeError("Could not connect to DB")  # все попытки мимо → честно падаем

@asynccontextmanager
async def lifespan(app: FastAPI):
    wait_for_db()    # ← код ДО yield выполняется при старте приложения
    yield            # ← здесь приложение работает
                     # ← код ПОСЛЕ yield выполнился бы при остановке

app = FastAPI(lifespan=lifespan)   # подключаем lifespan к приложению

@app.get("/health")
def health():
    return {"status": "ok"}