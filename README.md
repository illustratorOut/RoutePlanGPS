| Описание                 | Команды                        |
|--------------------------|--------------------------------|
| ✔️ Приминить миграции    | ```python manage.py migrate``` |
| ✔️ Создать пользователей | ```python manage.py ccsu```    |

<br>


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

API_KEY_2GIS=

CELERY_BROKER_URL=redis://redis:6379
CELERY_RESULT_BACKEND=redis://redis:6379
```

</div>
