from django.urls import path
from . import views


app_name = 'departamento_app'

urlpatterns = [
    path('listar', views.DepartamentoListView.as_view(), name='listar'),
    path('nuevo', views.NewDepatamentoView.as_view(), name='nuevo'),
]
