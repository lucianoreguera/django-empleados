from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba
from .forms import PruebaForm


class HomeView(TemplateView):
    """ Página de inicio del proyecto """
    template_name = 'home/index.html'

# Clases realizadas para ir probando conceptos
class PruebaView(TemplateView):
    template_name = 'home/prueba.html'

class ResumeFoundationView(TemplateView):
    template_name = 'home/resume_foundation.html'

class PruebaListView(ListView):
    # model = Prueba
    # Todavía no vimos modelos entonces podemos usar queryset
    template_name = "home/lista.html"
    context_object_name = 'listado'
    queryset = ['Luciano', 'María', 'Ignacio']

class ListarPrueba(ListView):
    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name = "listado"

class PruebaCreateView(CreateView):
    template_name = "home/crear.html"
    model = Prueba
    # Campos que voy a pedir para crear un elemento
    # fields = ['titulo', 'subtitulo', 'cantidad']
    form_class = PruebaForm
    success_url = 'home/prueba.html'
