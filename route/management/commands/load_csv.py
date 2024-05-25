import os
import aiofiles
import asyncio
import asyncpg
import csv

from colorama import Fore
from django.core.management import BaseCommand
from aiocsv import AsyncDictReader


class Command(BaseCommand):

    def handle(self, *args, **options):

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
            try:
                async with aiofiles.open(name, encoding='utf-8') as r_file:
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
                            for row in queries:
                                res = await connection.fetch(
                                    f'SELECT * FROM "route_gasstation" WHERE latitude={row[2]} AND longitude={row[1]}')
                                if res:
                                    print(f'\n{Fore.RED}Данные из файла "{name}" уже были загружены!\n{Fore.RESET}')
                                    break
                                else:
                                    await connection.executemany(
                                        'INSERT INTO "route_gasstation" (region, longitude, latitude, price_dt) VALUES ($1,$2 ,$3, $4)',
                                        queries)
                                    print(
                                        f'\n{Fore.GREEN}Загружено в БД {Fore.MAGENTA}{len(queries)}{Fore.RESET} {Fore.GREEN}заправок!{Fore.RESET}\n')
                                    break
            except Exception as e:
                print(f'\n{Fore.RED}Возникла ошибка при загрузке данных из файла {name} {Fore.RESET}{e}\n')

        asyncio.run(load_csv('spisokAZS.csv'))
