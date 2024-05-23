from json import dumps

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from route.forms import RouteForm
from route.models import Route, GasStation
from route.services import RouteMap
from colorama import Fore

import folium
import time
import requests


class RouteDetailView(DetailView):
    """Класс просмотра 1 маршрута"""
    model = Route


class RouteListView(ListView):
    """Класс отображения маршрута"""
    model = Route


class RouteCreateView(LoginRequiredMixin, CreateView):
    """Класс создания маршрута"""
    model = Route
    form_class = RouteForm
    success_url = reverse_lazy('route:home')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class RouteUpdateView(LoginRequiredMixin, UpdateView):
    """Класс редактирования маршрута"""
    model = Route
    form_class = RouteForm
    success_url = reverse_lazy('route:home')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        return form


class RouteDeleteView(LoginRequiredMixin, DeleteView):
    """Класс удаления маршрута"""
    model = Route
    success_url = reverse_lazy('route:home')


def render_map(request, pk):
    '''Генерация карты, получаем данны о маршруте через API'''

    items = GasStation.objects.all()
    route = Route.objects.filter(id=pk).first()
    map = RouteMap()

    if route:
        data = {
            "waypoints": [
                {
                    "longitude": route.start_points_x,
                    "latitude": route.start_points_y
                },
                {
                    "longitude": route.end_points_x,
                    "latitude": route.end_points_y
                }

            ],
            "vehicle_type": "truck",
            "jams": False,
            "truck_limits": {
                "total_weight_kg": route.mass,
                "axle_weight_kg": route.axle_load,
                "width_meters": route.width,
                "height_meters": route.height,
                "length_meters": route.length
            }
        }
        route_id = map.get_route_id(data)
        route_points = map.get_route_points(route_id)
        route_data = map.get_route_metadata(route_id)

        # Получаем координаты отправки и назначения
        x_start = data['waypoints'][0]['longitude']
        y_start = data['waypoints'][0]['latitude']

        x_end = data['waypoints'][1]['longitude']
        y_end = data['waypoints'][1]['latitude']

        n = route_data['duration_seconds']
        time_format = time.strftime("%H:%M:%S", time.gmtime(n))
        length_km = int(float(route_data['length_meters']) / 1000)

        map_title = f'{length_km}км Время: {time_format}'
        title_html = f'<h1 style="position:absolute;z-index:100000;left:40vw" >{map_title}</h1>'

        m = folium.Map(location=[y_start, x_start], zoom_start=5)

        figure = folium.FeatureGroup(name="Все метки")
        m.add_child(figure)
        loc = []

        for row in route_points[0]['points']:
            loc.append((float(row[1]), float(row[0])))

        m.get_root().html.add_child(folium.Element(title_html))

        folium.Marker(location=[y_start, x_start],
                      popup=str('А'),
                      icon=folium.Icon(color='black')
                      ).add_to(m)

        folium.Marker(location=[y_end, x_end],
                      popup=str('Б'),
                      icon=folium.Icon(color='black')
                      ).add_to(m)

        # # ---------------------------------------------------------------------------------
        # all_points = []
        #
        # def get_deviation_point(point_, percent_):
        #     # Процент отклонения
        #     percent = percent_
        #     x = point_[0]
        #     y = point_[1]
        #
        #     for row in route_points[0]['points']:
        #         point_x = round(row[0])
        #         point_y = round(row[1])
        #         point_max_x = round(point_x + (point_x * percent / 100))
        #         point_min_x = round(point_x - (point_y * percent / 100))
        #
        #
        #
        #         res = x in range(point_min_x, point_max_x)
        #         if res:
        #             print(res)
        #             all_points.append(res)
        #         else:
        #             pass

        for row in items:
            # lines = [{"q": f'{row.latitude},{row.longitude}'}]
            # weather = map.get_weather(lines)
            # try:
            #     res = weather[0]['temp_c']
            # except:
            #     res = '-'
            # print(weather)
            # '\nТемпература: {res}°C'

            folium.Marker(
                [row.longitude, row.latitude],
                popup=f'<strong>Цена ДТ: {row.price_dt}</strong>',
                tooltip='Заправка!',
                icon=folium.Icon(icon='cloud', color='lightgray')
            ).add_to(m)

        folium.PolyLine(loc,
                        color='red',
                        weight=5,
                        opacity=0.8).add_to(m)

        m.save(f"route/templates/map/map.html")
        return render(request, 'map/map.html')

    return render(request, 'route/route_list.html')
