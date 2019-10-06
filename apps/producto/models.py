from django.db import models
from apps.retiro.models import retiro

# Create your models here.

class accesorio(models.Model):
    tipo = models.CharField(max_length=50)

class articulo(models.Model):
    tipo_art = models.CharField(max_length=50)
    talla = models.CharField(max_length=3)
    color = models.CharField(max_length=10)
    fecha_llegada = models.DateField()
    cantidad = models.IntegerField()
    retiro = models.ForeignKey(retiro, null=True, blank=True, on_delete=models.CASCADE)
    accesorio = models.ManyToManyField(accesorio)


