# Generated by Django 4.2.13 on 2024-05-21 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0004_alter_route_end_points_x_alter_route_end_points_y_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GasStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.TextField(verbose_name='Регион')),
            ],
            options={
                'verbose_name': 'Заправка',
                'verbose_name_plural': 'Заправки',
            },
        ),
    ]
