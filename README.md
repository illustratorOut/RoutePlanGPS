# Грузовые GPS маршруты

Предлагается веб-приложения, прокладка маршрута по РФ с отображением АЗС по пути следования грузовых авто.

## Содержание

- [Технологии](#технологии)
- [Начало работы](#Разработка)
- [Примеры использования](#Использование)

## Технологии

- [DJANGO](https://www.djangoproject.com/)
- [DJANGO REST FRAMEWORK](https://www.django-rest-framework.org/)
- [DRF-YASG](https://drf-yasg.readthedocs.io/en/stable/readme.html)
- [NAVITEL API](https://навител.рф/ru/apinavitelmaps/api)
- [WEATHER API](https://www.weatherapi.com/docs/#)
- [PSYCOPG2](https://www.psycopg.org/)
- [FOLIUM](https://python-visualization.github.io/folium/latest/)
- [SIMPLEJWT](https://github.com/jazzband/djangorestframework-simplejwt)
- ...

## Разработка

### Требования

Для установки и запуска проекта, необходим [Python](https://www.python.org/downloads/)
v3.12, [PostgreSQL](https://www.postgresql.org/download/windows/) 15.7

### Установка зависимостей

Для установки зависимостей, выполните команду:

```pip install -r .\requirements.txt ```

Создайте файл с названием ".env" и заполните пустые поля:

<H3 style="text-align: center; color:#A7FC00;">Шаблон для файла .env </H3>
<div style="display: flex; justify-content: center;">

```dotenv
CACHE_ENABLED=True
REDIS=redis://127.0.0.1:6379

POSTGRES_DB=
POSTGRES_PASSWORD=
POSTGRES_USER=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=

API_KEY_NAVITEL=
API_KEY_WEATHER=

CELERY_BROKER_URL=redis://redis:6379
CELERY_RESULT_BACKEND=redis://redis:6379
```

</div>

Выполните команды из примера ниже:
<br>

| Описание                   | Команды                                                    |
|----------------------------|------------------------------------------------------------|
| ✔️ Приминить миграции      | ```python manage.py migrate```                             |
| ✔️ Создать пользователей   | ```python manage.py ccsu```                                |
| ✔️ Создать маршруты        | ```python manage.py route_data```                          |
| ✔️ Загрузить в БД заправки | ```python manage.py load_csv```                            |
| ✔️ Запустить HTTPS         | ```python manage.py runserver_plus --cert-file cert.crt``` |

<br>

## Использование

> [!TIP]
> 1. Перед использованием проекта оснакомпесь с вспомогательным контентом
> 2. Выполните все команды из таблицы ниже или разверните докер контейнер

## FAQ
