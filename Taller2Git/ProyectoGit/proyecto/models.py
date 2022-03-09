from django.db import models

Class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)

Class Actividad(models.Model):
    nombre = models.CharField(max_length=200)
    calificacion = models.IntegerField()# 0-10
