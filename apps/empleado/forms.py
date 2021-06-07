from django import forms
from .models import Empleado

# Para mostrar las habilidades de una manera diferente a la que proponer form por defecto
class EmpleadoForm(forms.ModelForm):
    
    class Meta:
        model = Empleado
        fields = (
            'first_name',
            'last_name',
            'job',
            'departamento',
            'avatar',
            'habilidades'
        )
        widgets = {
            'habilidades': forms.CheckboxSelectMultiple()
        }
