from flask import Flask
import redis
import os

app = Flask(__name__)

try:
    cache = redis.Redis(host='redis', port=6379)
except Exception:
    cache = None

@app.route('/')
def hello():
    count = "nieznana"
    if cache:
        try:
            cache.incr('hits')
            count = cache.get('hits').decode('utf-8')
        except redis.exceptions.ConnectionError:
            count = "błąd połączenia z Redis"
            
    return f"Witaj! Liczba odwiedzin: {count}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)