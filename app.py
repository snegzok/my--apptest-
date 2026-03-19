from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    # Получаем имя контейнера (обычно это его ID)
    hostname = socket.gethostname()
    return f"""
    <h1>Привет от DevOps-стажёра! 🚀</h1>
    <p>Приложение работает внутри Docker-контейнера.</p>
    <p><b>ID контейнера:</b> {hostname}</p>
    <p><b>Версия:</b> 1.0.0</p>
    """

if __name__ == "__main__":
    # Слушаем на всех интерфейсах (0.0.0.0) внутри контейнера
    app.run(host="0.0.0.0", port=8080)
