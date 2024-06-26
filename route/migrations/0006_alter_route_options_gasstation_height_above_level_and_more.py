# Generated by Django 4.2.13 on 2024-05-23 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0005_gasstation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='route',
            options={'verbose_name': 'Маршрут', 'verbose_name_plural': 'Маршруты'},
        ),
        migrations.AddField(
            model_name='gasstation',
            name='height_above_level',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Высота над уровнем моря'),
        ),
        migrations.AddField(
            model_name='gasstation',
            name='latitude',
            field=models.FloatField(default=0, verbose_name='Широта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gasstation',
            name='longitude',
            field=models.FloatField(default=0, verbose_name='Долгота'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gasstation',
            name='price_dt',
            field=models.FloatField(blank=True, null=True, verbose_name='Стоимость ДТ'),
        ),
        migrations.AddField(
            model_name='gasstation',
            name='temperature',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Температура'),
        ),
    ]
