from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import NewDepartamentoForm
from .models import Departamento
from apps.empleado.models import Empleado



class DepartamentoListView(ListView):
    template_name = "departamento/list.html"
    model = Departamento
    context_object_name = 'departamentos'


class NewDepatamentoView(FormView):
    template_name = 'departamento/new_dpto.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        firstname  = form.cleaned_data['first_name']
        lastname  = form.cleaned_data['last_name']
        dpto = Departamento(
                name = form.cleaned_data['departamento'],
                short_name = form.cleaned_data['short_name']
            )
        dpto.save()
        
        Empleado.objects.create(
            first_name = firstname,
            last_name = lastname,
            job = '1',
            departamento = dpto
        )

        return super().form_valid(form)
