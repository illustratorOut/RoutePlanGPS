import os
import requests

from json import dumps
from colorama import Fore
from dotenv import load_dotenv

load_dotenv()


class RouteMap:
    url_route_id = 'https://webmapapi.navitel.ru/api/v1/routeId'
    url_route_metadata = 'https://webmapapi.navitel.ru/api/v1/routeMetadata'
    url_route_points = 'https://webmapapi.navitel.ru/api/v1/routeGeometry'
    url_weather = "http://api.weatherapi.com/v1/current.json?q=bulk"

    headers = {
        'accept': 'application/json',
        'Api-Key': os.getenv('API_KEY_NAVITEL'),
        'Content-Type': 'application/json'
    }

    def __init__(self):
        pass

    def get_route_id(self, data: dict) -> str:
        '''Уникальный идентификатор маршрута'''
        try:
            response = requests.post(url=self.url_route_id, data=dumps(data), headers=self.headers)
            result = response.json()
            return result.get('route_id')
        except:
            return False

    def get_route_metadata(self, route_id: str) -> dict:
        '''Метаданные маршрута'''
        response = requests.post(url=self.url_route_metadata, data=dumps({"route_id": route_id}), headers=self.headers)
        result = response.json()
        return result

    def get_route_points(self, route_id: str) -> list:
        '''Геометрия маршрута'''
        response = requests.post(url=self.url_route_points, data=dumps({"route_id": route_id}), headers=self.headers)
        result = response.json().get('lines')
        return result

    def get_weather(self, line: list) -> list:
        '''Получить прогноз погоды'''
        headers = {
            'key': os.getenv('API_KEY_WEATHER'),
            'Content-Type': 'application/json'
        }

        data = {"locations": [*line]}
        response = requests.post(url=self.url_weather, data=dumps(data), headers=headers)
        result = response.json()

        res = []
        try:
            for row in result['bulk']:
                temp_c = row['query']['current']['temp_c']
                city = row['query']['location']['name']
                res.append({'city': city, 'temp_c': temp_c})
        except Exception as e:
            print(f'{Fore.RED}Возникла ошибка при получении прогноза погоды\n{Fore.RESET}{e}')
        return res
