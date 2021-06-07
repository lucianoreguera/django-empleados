from django.db import models


class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre corto', max_length=30)
    is_active = models.BooleanField('Activado', default=False)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['name']
        unique_together = ('name', 'short_name')
    
    def __str__(self):
        return self.name
    