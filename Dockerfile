# Указываем базовый образ
FROM python:3.10-slim

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Установим зависимости
WORKDIR /app

# Копируем файл зависимостей
COPY ./requirements.txt /requirements.txt

# Устанавливаем системные зависимости
RUN pip install --upgrade pip && pip install --no-cache-dir -r /requirements.txt

# Копируем файлы проекта в рабочий каталог
COPY ./app /app/

# Открываем порт на контейнере
EXPOSE 8000
