from rest_framework.generics import RetrieveAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from route.models import Route
from route.permissions import IsOwner
from route.seriallizers.route import RouteSerializer, RouteCreateSerializer


class RouteDetailAPIView(RetrieveAPIView):
    '''Отображение маршрута'''
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class RouteListAPIView(ListAPIView):
    '''Отображение списка маршрутов'''
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [IsAuthenticated]


class RouteCreateAPIView(CreateAPIView):
    '''Создание маршрута'''
    queryset = Route.objects.all()
    serializer_class = RouteCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        '''При создании маршрута присваиваем автора(user)'''
        route_ = serializer.save()
        route_.user = self.request.user
        route_.save()


class RouteUpdateAPIView(UpdateAPIView):
    '''Редактирование (обновление) маршрута'''
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class RouteDeleteAPIView(DestroyAPIView):
    '''Удаление маршрута'''
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [IsAuthenticated, IsOwner]
