# from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    TemplateView, 
    DeleteView
)
from django.urls import reverse_lazy
from .models import Empleado
from .forms import EmpleadoForm


# Listar todos los empleados
class ListAllEmpleados(ListView):
    template_name = 'empleado/list-all.html'
    paginate_by = 5
    ordering = 'last_name'
    context_object_name = 'empleados'

    def get_queryset(self):
        # Segndo parametro vacio para que no de error None y muestre todos
        full_name = self.request.GET.get('keyword', '')
        list = Empleado.objects.filter(full_name__icontains = full_name)
        return list


class ListAllEmpleadosAdmin(ListView):
    template_name = 'empleado/list-all-admin.html'
    paginate_by = 10
    ordering = 'last_name'
    context_object_name = 'empleados'
    model = Empleado


# Listar todos los empleados de un área específica
class ListByAreaEmpleados(ListView):
    template_name = 'empleado/list-by-area.html'
    # queryset = Empleado.objects.filter(departamento__name='Area Finanzas')
    context_object_name = 'empleados'

    def get_queryset(self):
        area = self.kwargs['area']
        list = Empleado.objects.filter(departamento__short_name=area)
        return list


# Listar empleados según una palabra clave - búsqueda por form html
class ListByKeywordEmpleados(ListView):
    template_name = 'empleado/list-by-keyword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        name = self.request.GET.get('keyword')
        list = Empleado.objects.filter(first_name__icontains = name)
        return list


class ListHabilidadesEmpleado(ListView):
    template_name = 'empleado/list-skills.html'
    context_object_name = 'skills'

    def get_queryset(self):
        pk = self.kwargs['pk']
        employee = Empleado.objects.get(id=pk)
        return employee.habilidades.all()


# Detalle empleado
class DetailEmpleado(DetailView):
    model = Empleado
    template_name = 'empleado/detail.html'
    context_object_name = 'empleado'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 
        context['title'] = 'Empleado del mes'
        # 
        return context


# Registrar un nuevo empleado
class CreateEmpleado(CreateView):
    template_name = 'empleado/create.html'
    model = Empleado
    form_class = EmpleadoForm
    # fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades', 'avatar']
    # fields = ('__all__')
    # success_url = '.'
    # success_url = '/empleados/success'
    success_url = reverse_lazy('empleado_app:listar_admin')

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        # Funciona de las 2 formas, super sin parametros y con parametros
        return super(CreateEmpleado, self).form_valid(form)
        # return super().form_valid(form)


# Template de registro exitoso
class Success(TemplateView):
    template_name = 'empleado/success.html'


# Actualizar un empleado
class UpdateEmpleado(UpdateView):
    model = Empleado
    template_name = 'empleado/update.html'
    # fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades', 'avatar']
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleado_app:listar_admin')

    def post(self, request, *args, **kwargs):
        
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        
        return super().form_valid(form)

# Eliminar un empleado
class DeleteEmpleado(DeleteView):
    model = Empleado
    template_name = 'empleado/delete.html'
    success_url = reverse_lazy('empleado_app:listar_admin')