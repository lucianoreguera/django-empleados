from django.urls import path
from . import views


app_name = 'empleado_app'

urlpatterns = [
    path('listar/', views.ListAllEmpleados.as_view(), name='listar'),
    path('listar/<str:area>/', views.ListByAreaEmpleados.as_view(), name='listar_por_area'),
    path('listar-admin/', views.ListAllEmpleadosAdmin.as_view(), name='listar_admin'),
    path('buscar/', views.ListByKeywordEmpleados.as_view()),
    path('<int:pk>/habilidades/', views.ListHabilidadesEmpleado.as_view()),
    path('detalle/<int:pk>', views.DetailEmpleado.as_view(), name='detalle'),
    path('crear/', views.CreateEmpleado.as_view(), name='registrar'),
    path('success/', views.Success.as_view(), name='correcto'),
    path('<int:pk>/actualizar/', views.UpdateEmpleado.as_view(), name='actualizar'),
    path('<int:pk>/eliminar/', views.DeleteEmpleado.as_view(), name='eliminar'),
]
