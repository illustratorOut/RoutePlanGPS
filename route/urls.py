from django.urls import path

from route.apps import RouteConfig
from route.views.route import RouteListView, RouteCreateView, RouteUpdateView, RouteDeleteView, RouteDetailView

app_name = RouteConfig.name

urlpatterns = [
    path('', RouteListView.as_view(), name='home'),
    path('view/<int:pk>', RouteDetailView.as_view(), name='view'),
    path('create/', RouteCreateView.as_view(), name='create'),
    path('update/<int:pk>/', RouteUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', RouteDeleteView.as_view(), name='delete'),

]
