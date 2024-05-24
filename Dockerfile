# Используем базовый образ Python
FROM python:3

# Устанавливаем рабочую директорию в контейнере
WORKDIR /code

# Копируем зависимости и код приложения
COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .


