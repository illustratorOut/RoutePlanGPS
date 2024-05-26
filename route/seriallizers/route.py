from rest_framework import serializers
from route.models import Route
from route.validators import TruckLengthValidator, TruckHeightValidator, TruckWidthValidator, TruckMassValidator, \
    TruckAxleLoadValidator, TruckMaxPermMassValidator, PointParamsValidator


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        exclude = ('user', 'last_update')


class RouteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'
        validators = [
            TruckLengthValidator(field='length'),
            TruckHeightValidator(field='height'),
            TruckWidthValidator(field='width'),
            TruckMassValidator(field='mass'),
            TruckMaxPermMassValidator(field='max_perm_mass'),
            TruckAxleLoadValidator(field='axle_load'),

            PointParamsValidator(field1='start_points_x',
                                 field2='start_points_y',
                                 field3='end_points_x',
                                 field4='end_points_y',
                                 ),
        ]
