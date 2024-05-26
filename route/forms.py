from django import forms
from route.models import Route
from users.forms import StyleFormMixin


class RouteForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Route
        exclude = ('user', 'start_title', 'end_title')

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
                    'placeholder': "Длина, метры",
                    'step': '0.000001'
                }),

            'width': forms.NumberInput(
                attrs={
                    'type' : "text",
                    'class': "form-control",
                    'min': 0,
                    'placeholder': "Ширина, метры",
                    'step': '0.000001'
                }),

            'height': forms.NumberInput(
                attrs={
                    'min': 0,
                    'placeholder': "Высота, метры",
                    'step': '0.000001'
                }),

            'mass': forms.NumberInput(
                attrs={
                    'min': 0,
                    'placeholder': "Фактическая масса, тонны",
                    'step': '0.000001'
                }),

            'max_perm_mass': forms.NumberInput(
                attrs={
                    'min': 0,
                    'placeholder': "Разрешённая масса, тонны",
                    'step': '0.000001'
                }),

            'axle_load': forms.NumberInput(
                attrs={
                    'min': 0,
                    'placeholder': "Максимальная нагрузка на ось, тонны",
                    'step': '0.000001'
                }),
            'status_jams': forms.CheckboxInput(
                attrs={
                    'class': "form-check-input",
                    'type': "checkbox"
                }),

        }
