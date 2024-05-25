from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}


class Route(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    start_title = models.TextField(verbose_name='Название отправления маршрута', **NULLABLE)
    end_title = models.TextField(verbose_name='Название прибытия маршрута', **NULLABLE)
    start_points_x = models.CharField(max_length=120, verbose_name='Координаты города отправки x')
    start_points_y = models.CharField(max_length=120, verbose_name='Координаты города отправки y')
    end_points_x = models.CharField(max_length=120, verbose_name='Координаты города прибытия x')
    end_points_y = models.CharField(max_length=120, verbose_name='Координаты города прибытия y')
    length = models.FloatField(verbose_name='Длина')
    height = models.FloatField(verbose_name='Высота')
    width = models.FloatField(verbose_name='Ширина')
    mass = models.FloatField(verbose_name='Фактическая масса')
    max_perm_mass = models.FloatField(verbose_name='Разрешённая масса')
    axle_load = models.FloatField(verbose_name='Максимальная нагрузка на ось')
    status_jams = models.BooleanField(default=False, verbose_name='Учитывать пробки', **NULLABLE)
    last_update = models.DateTimeField(auto_now_add=True, verbose_name='Последнее обновление', **NULLABLE)

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'


class GasStation(models.Model):
    region = models.TextField(verbose_name='Регион')
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')
    price_dt = models.FloatField(verbose_name='Стоимость ДТ', **NULLABLE)
    height_above_level = models.CharField(max_length=120, verbose_name='Высота над уровнем моря', **NULLABLE)
    temperature = models.CharField(max_length=120, verbose_name='Температура', **NULLABLE)

    class Meta:
        verbose_name = 'Заправка'
        verbose_name_plural = 'Заправки'
