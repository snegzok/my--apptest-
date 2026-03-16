# Базовый образ с Python
FROM python:3.9-slim

# Папка внутри контейнера
WORKDIR /app

# Копируем список зависимостей и ставим их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь остальной код (app.py)
COPY . .

# Открываем порт
EXPOSE 8080

# Запускаем приложение
CMD ["python", "app.py"]
