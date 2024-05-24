from django.urls import path

from route.apps import RouteConfig
from route.views.API_route import RouteDetailAPIView, RouteCreateAPIView, RouteUpdateAPIView, \
    RouteDeleteAPIView, RouteListAPIView
from route.views.route import RouteListView, RouteCreateView, RouteUpdateView, RouteDeleteView, render_map

app_name = RouteConfig.name

urlpatterns = [
    path('', RouteListView.as_view(), name='home'),
    path('view/<int:pk>', render_map, name='view'),
    path('create/', RouteCreateView.as_view(), name='create'),
    path('update/<int:pk>/', RouteUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', RouteDeleteView.as_view(), name='delete'),

    # API Route
    path('API/', RouteListAPIView.as_view()),
    path('API/<int:pk>/', RouteDetailAPIView.as_view()),
    path('API/create/', RouteCreateAPIView.as_view()),
    path('API/update/<int:pk>/', RouteUpdateAPIView.as_view()),
    path('API/delete/<int:pk>/', RouteDeleteAPIView.as_view()),

]
