from django.urls import path
from . import views


app_name = 'home_app'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # Urls utilizadas para ir probando conceptos
    path('home/prueba', views.PruebaView.as_view()),
    path('home/listado', views.PruebaListView.as_view()),
    path('home/list_view', views.ListarPrueba.as_view()),
    path('home/create_view', views.PruebaCreateView.as_view()),
    path(
        'home/resume_foundation', 
        views.ResumeFoundationView.as_view(), 
        name='resume_foundation'
    ),
]
