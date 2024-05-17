from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}


class Route(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
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
    last_update = models.DateTimeField(auto_now_add=True, verbose_name='Последнее обновление', **NULLABLE)

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруту'


class GasStation(models.Model):
    region = models.TextField(verbose_name='Регион')

    class Meta:
        verbose_name = 'Заправка'
        verbose_name_plural = 'Заправки'
