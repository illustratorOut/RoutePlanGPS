import datetime

from django import forms
from django.core.exceptions import ValidationError

from route.models import Route
from users.forms import StyleFormMixin


class RouteForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Route
        exclude = ('user',)

        labels = {
            'start_points_x': '',
            'start_points_y': '',
            'end_points_x': '',
            'end_points_y': '',
            'height': '',
            'length': '',
            'width': '',
            'mass': '',
            'max_perm_mass': '',
            'axle_load': '',
        }

        widgets = {
            'start_points_x': forms.NumberInput(
                attrs={
                    'min': 0,
                    'placeholder': 'Координаты X: Долгота',
                    'step': '0.000001',
                }),

            'start_points_y': forms.NumberInput(
                attrs={
                    'min': 0,
                    'placeholder': 'Координаты Y: Широта',
                    'step': '0.000001',
                }),

            'end_points_x': forms.NumberInput(
                attrs={
                    'min': 0,
                    'placeholder': 'Координаты X: Долгота',
                    'step': '0.000001',
                }),

            'end_points_y': forms.NumberInput(
                attrs={
                    'min': 0,
                    'placeholder': 'Координаты Y: Широта',
                    'step': '0.000001',
                }),

            'length': forms.NumberInput(
                attrs={
                    'min': 0,
                    'placeholder': "Длина",
                    'step': '0.1'
                }),

            'width': forms.NumberInput(
                attrs={
                    'min': 0,
                    'placeholder': "Ширина",
                    'step': '0.1'
                }),

            'height': forms.NumberInput(
                attrs={
                    'min': 0,
                    'placeholder': "Высота",
                    'step': '0.1'
                }),

            'mass': forms.NumberInput(
                attrs={
                    'min': 0,
                    'placeholder': "Фактическая масса",
                    'step': '0.1'
                }),

            'max_perm_mass': forms.NumberInput(
                attrs={
                    'min': 0,
                    'placeholder': "Разрешённая масса",
                    'step': '0.1'
                }),

            'axle_load': forms.NumberInput(
                attrs={
                    'min': 0,
                    'placeholder': "Максимальная нагрузка на ось",
                    'step': '0.1'
                }),
        }
