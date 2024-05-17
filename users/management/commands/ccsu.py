from colorama import Fore
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        dict_user = {
            'user_admin': {
                'email': 'admin@sky.pro',
                'first_name': 'Admin',
                'last_name': 'Adminov',
                'is_superuser': True,
                'is_staff': True,
                'is_active': True,
                'password': '1234S5678'},

            'user_moder': {
                'email': 'manager@sky.pro',
                'first_name': 'Manager',
                'last_name': 'Managers',
                'is_active': True,
                'password': '1234S5678'},

            'user_uses': {
                'email': 'user@sky.pro',
                'first_name': 'User',
                'last_name': 'Users',
                'is_active': True,
                'password': '1234S5678'},
        }

        for row in dict_user:
            email = dict_user[row]['email']
            password = dict_user[row]['password']

            if User.objects.filter(email=email):
                print(
                    f'Пользователь {Fore.RED}{email}{Fore.RESET} уже существует! password: ({Fore.GREEN}{password}{Fore.RESET})')
            else:
                user = User.objects.create(**dict_user[row])
                user.set_password(password)
                user.save()
                print(
                    f'{Fore.GREEN}Пользователь создан!\n {Fore.RESET}login: {Fore.GREEN} {user.email}\n {Fore.RESET}password: {Fore.GREEN}{password}{Fore.RESET}\n')
