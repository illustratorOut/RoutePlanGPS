import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from route.forms import RouteForm
from route.models import Route


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
