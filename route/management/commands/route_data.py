from colorama import Fore
from django.core.management import BaseCommand

from route.models import Route
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            users = User.objects.all()
            for user in users:
                dict_route = {
                    'route1': {
                        'user': user,
                        'start_title': 'Барнаул',
                        'end_title': 'Дербент',
                        'start_points_x': '83.7636',
                        'start_points_y': '53.3606',
                        'end_points_x': '48.2899',
                        'end_points_y': '42.0678',
                        'length': 0,
                        'height': 4,
                        'width': 0,
                        'mass': 44,
                        'max_perm_mass': 0,
                        'axle_load': 9
                    },

                    'route2': {
                        'user': user,
                        'start_title': 'Ростов-на-Дону',
                        'end_title': 'Владивосток',
                        'start_points_x': '39.7233',
                        'start_points_y': '47.2313',
                        'end_points_x': '131.874',
                        'end_points_y': '43.1056',
                        'length': 0,
                        'height': 4,
                        'width': 0,
                        'mass': 44,
                        'max_perm_mass': 0,
                        'axle_load': 9
                    },

                    'route3': {
                        'user': user,
                        'start_title': 'Владивосток',
                        'end_title': 'Дербент',
                        'start_points_x': '131.874',
                        'start_points_y': '43.1056',
                        'end_points_x': '48.2899',
                        'end_points_y': '42.0678',
                        'length': 0,
                        'height': 4,
                        'width': 0,
                        'mass': 44,
                        'max_perm_mass': 0,
                        'axle_load': 9
                    },
                }

                for row in dict_route:
                    if Route.objects.filter(
                            user=dict_route[row]['user'],
                            start_title=dict_route[row]['start_title'],
                            end_title=dict_route[row]['end_title'],
                            start_points_x=dict_route[row]['start_points_x'],
                            start_points_y=dict_route[row]['start_points_y'],
                            end_points_x=dict_route[row]['end_points_x'],
                            end_points_y=dict_route[row]['end_points_y']):
                        print(
                            f'Маршрут  {Fore.RED}{dict_route[row]['start_title']} → {dict_route[row]['end_title']}{Fore.RESET} уже существует!')
                    else:
                        route = Route.objects.create(**dict_route[row])
                        route.save()
                        print(f'Для пользователя: {Fore.GREEN}{user}{Fore.RESET} создан 1 маршрут!')
        except Exception as e:
            print(f'{Fore.RED}Возникла ошибка при создании маршрутов пользователю\n{Fore.RESET}{e}')
