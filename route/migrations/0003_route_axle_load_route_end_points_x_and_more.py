# Generated by Django 4.2.13 on 2024-05-14 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='axle_load',
            field=models.FloatField(default=0, verbose_name='Максимальная нагрузка на ось'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='end_points_x',
            field=models.FloatField(default=0, verbose_name='Координаты города прибытия x'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='end_points_y',
            field=models.FloatField(default=0, verbose_name='Координаты города прибытия y'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='height',
            field=models.FloatField(default=0, verbose_name='Высота'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='length',
            field=models.FloatField(default=0, verbose_name='Длина'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='mass',
            field=models.FloatField(default=0, verbose_name='Фактическая масса'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='max_perm_mass',
            field=models.FloatField(default=0, verbose_name='Разрешённая масса'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='start_points_x',
            field=models.FloatField(default=0, verbose_name='Координаты города отправки x'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='start_points_y',
            field=models.FloatField(default=0, verbose_name='Координаты города отправки y'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='width',
            field=models.FloatField(default=0, verbose_name='Ширина'),
            preserve_default=False,
        ),
    ]