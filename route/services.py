import os
import aiofiles
import asyncpg
import requests
import csv

from json import dumps
from aiocsv import AsyncDictReader
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
        response = requests.post(url=self.url_route_id, data=dumps(data), headers=self.headers)
        result = response.json()
        return result.get('route_id')

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
            pass
        return res


def clear_str(row: str) -> str:
    '''Очищает строку row от заданных символов'''
    symbols = [' руб.', ' белор.', ',']
    row_clear = str(row).strip().lower()
    for symbol in symbols:
        if symbol in row_clear:
            if symbol == ',':
                row_clear = row_clear.replace(symbol, '.')
            else:
                row_clear = row_clear.replace(symbol, '')
    return row_clear


async def load_csv(name: str):
    '''Асинхронная загрузка данных (о заправках) в БД из файла CSV'''
    async with aiofiles.open(name) as r_file:
        dict_ = AsyncDictReader(r_file, delimiter=";", quoting=csv.QUOTE_ALL)

        queries = []
        async for row in dict_:
            if row['ДТ'] != '':
                queries.append(
                    (
                        row['Регион'],
                        float(clear_str(row['Координаты GPS (широта)'])),
                        float(clear_str(row['Координаты GPS (долгота)'])),
                        float(clear_str(row['ДТ']))
                    ))
            else:
                queries.append(
                    (
                        row['Регион'],
                        float(clear_str(row['Координаты GPS (широта)'])),
                        float(clear_str(row['Координаты GPS (долгота)'])),
                        0
                    ))

        async with asyncpg.create_pool(
                user=os.getenv('POSTGRES_USER'),
                password=os.getenv('POSTGRES_PASSWORD'),
                database=os.getenv('POSTGRES_DB'),
                host=os.getenv('POSTGRES_HOST'),
        ) as pool:
            async with pool.acquire() as connection:
                await connection.executemany(
                    'INSERT INTO "route_gasstation" (region, longitude, latitude, price_dt) VALUES ($1,$2 ,$3, $4)',
                    queries)

# asyncio.run(load_csv(r'C:\Users\Alex\PycharmProjects\RoutePlanGPS\spisokAZS.csv'))
