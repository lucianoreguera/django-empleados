from django.contrib import admin
from django.db import models
from .models import Empleado, Habilidades


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name'
    )
    search_fields = ['last_name']
    list_filter = ['job', 'habilidades']
    filter_horizontal = ['habilidades']

    def full_name(self, obj):
        # print(obj)
        return obj.first_name + ' ' + obj.last_name


admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidades)
