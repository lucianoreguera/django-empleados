# Generated by Django 3.2.3 on 2021-05-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('short_name', models.CharField(max_length=30, verbose_name='Nombre corto')),
                ('is_active', models.BooleanField(default=False, verbose_name='Activado')),
            ],
        ),
    ]
