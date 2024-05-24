from rest_framework.exceptions import ValidationError


class TruckLengthValidator:
    '''Проверка поля length на принадлежность к типу float'''

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        length = str(value.get('length'))

        try:
            length.replace(".", "", 1).isdigit()
        except:
            raise ValidationError('Параметр Длинны должен быть числом')


class TruckHeightValidator:
    '''Проверка поля height на принадлежность к типу float'''

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        height = str(value.get('height'))

        try:
            height.strip().replace(".", "", 1).isdigit()
        except:
            raise ValidationError('Параметр Высоты должен быть числом')


class TruckWidthValidator:
    '''Проверка поля width на принадлежность к типу float'''

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        width = str(value.get('width'))

        try:
            width.strip().replace(".", "", 1).isdigit()
        except:
            raise ValidationError('Параметр Ширина должен быть числом')


class TruckMassValidator:
    '''Проверка поля mass на принадлежность к типу float'''

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        mass = str(value.get('mass'))

        try:
            mass.strip().replace(".", "", 1).isdigit()
        except:
            raise ValidationError('Параметр Фактическая масса должен быть числом')


class TruckMaxPermMassValidator:
    '''Проверка поля max_perm_mass на принадлежность к типу float'''

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        max_perm_mass = str(value.get('max_perm_mass'))

        try:
            max_perm_mass.strip().replace(".", "", 1).isdigit()
        except:
            raise ValidationError('Параметр Разрешённая масса должен быть числом')


class TruckAxleLoadValidator:
    '''Проверка поля axle_load на принадлежность к типу float'''

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        axle_load = str(value.get('axle_load'))

        try:
            axle_load.strip().replace(".", "", 1).isdigit()
        except:
            raise ValidationError('Параметр Максимальная нагрузка на ось должен быть числом')


class PointParamsValidator:
    '''Проверка поля на валидность'''

    def __init__(self, field1, field2, field3, field4):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3
        self.field4 = field4

    def __call__(self, value):
        start_points_x = value.get('start_points_x')
        start_points_y = value.get('start_points_y')
        end_points_x = value.get('end_points_x')
        end_points_y = value.get('end_points_y')

        if None in [start_points_x, start_points_y, end_points_x, end_points_y]:
            raise ValidationError(
                f'Одно из полей не заполнено: "start_points_x","start_points_y","end_points_x","end_points_y"')

        try:
            count = 120

            result = [
                start_points_x.strip().replace(".", "", 1).isdigit(),
                start_points_y.strip().replace(".", "", 1).isdigit(),
                end_points_x.strip().replace(".", "", 1).isdigit(),
                end_points_y.strip().replace(".", "", 1).isdigit()
            ]

            if 0 >= len(start_points_x):
                raise ValidationError(f'Длинна символов не должна превышать {count} символов')
            elif False in result:
                raise ValidationError('В строке должено быть чиловое значение')
            elif len(start_points_x) > count:
                raise ValidationError(f'Длинна символов не должна превышать {count} символов')

        except Exception as e:
            raise ValidationError(f'Возникла ошибка {e}')
