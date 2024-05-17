from django.contrib.auth.models import AbstractUser
from django.db import models

from route.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    login = models.CharField(max_length=120, verbose_name='Логин')
    photo = models.ImageField(upload_to='users', verbose_name='Фотография', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
