# Generated by Django 4.2.13 on 2024-05-13 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Последнее обновление')),
            ],
            options={
                'verbose_name': 'Маршрут',
                'verbose_name_plural': 'Маршруту',
            },
        ),
    ]