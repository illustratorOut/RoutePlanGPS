from json import dumps
import folium
import requests

url = 'https://routing.api.2gis.com/truck/6.0.0/global?key=rurbbn3446&r=3270310259'

data = {
    "locale": "ru",
    "point_a_name": "Source",
    "point_b_name": "Target",
    "points": [{"type": "pedo", "x": 83.77921499999999, "y": 53.34895, "object_id": "3378322490785844"},
               {"type": "pedo", "x": 48.29643, "y": 42.063977, "object_id": "563572723679253"}],
    "purpose": "autoSearch",
    "type": "truck_jam",
    "alternative": 0,
    "viewport": {"topLeft": {"x": 83.77921499999999, "y": 53.34895},
                 "bottomRight": {"x": 48.29643, "y": 42.063977}, "zoom": 5.23436876515864},
    "truck_params": {"length": 3.8, "height": 4, "width": 2.1, "mass": 44, "max_perm_mass": 3.5, "axle_load": 9}
}

response = requests.post(url=url, data=dumps(data))

res = response.json()

# Получаем координаты отправки и назначения
x_start = res['query']['points'][0]['x']
y_start = res['query']['points'][0]['y']

x_end = res['query']['points'][1]['x']
y_end = res['query']['points'][1]['y']

value = res['result'][0]['ui_total_distance']['value']
unit = res['result'][0]['ui_total_distance']['unit']
ui_total_duration = res['result'][0]['ui_total_duration']
zoom_start = res['query']['viewport']['zoom']

map_title = f'{value} {unit} Время: {ui_total_duration}'
title_html = f'<h1 style="position:absolute;z-index:100000;left:40vw" >{map_title}</h1>'

m = folium.Map(location=[y_start, x_start],
               zoom_start=zoom_start, )

figure = folium.FeatureGroup(name="Все метки")
m.add_child(figure)
loc = []

for row in res['result'][0]['maneuvers']:

    if row.get('outcoming_path') is not None:
        res = row.get('outcoming_path').get('geometry')[0].get('selection')
        str_res = str(res).replace('LINESTRING(', '').replace(')', '')

        for i in str_res.split(','):
            x, y = i.strip().split(' ')
            loc.append((float(y), float(x)))

m.get_root().html.add_child(folium.Element(title_html))

folium.Marker(location=[y_start, x_start],
              popup=str('А'),
              icon=folium.Icon(color='black')
              ).add_to(m)

folium.Marker(location=[y_end, x_end],
              popup=str('Б'),
              icon=folium.Icon(color='black')
              ).add_to(m)

folium.PolyLine(loc,
                color='red',
                weight=5,
                opacity=0.8).add_to(m)
m.save("map1.html")
