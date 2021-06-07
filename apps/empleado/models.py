from django.db import models
from apps.departamento.models import Departamento
from ckeditor.fields import RichTextField


class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleado'

    def __str__(self):
        return self.habilidad
    

class Empleado(models.Model):
    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    )

    first_name = models.CharField('Nombre/s', max_length=60)
    last_name = models.CharField('Apellido/s', max_length=60)
    full_name = models.CharField('Nombre completo', max_length=120, blank=True)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, verbose_name='Departamento', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    cv = RichTextField()

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['last_name']
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return self.last_name + ', ' + self.first_name
