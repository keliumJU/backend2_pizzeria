from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
#from tareas.models import Categorias
#from nombre_app.nombre_modulo import nombre clase ...
from django.utils import timezone
import os
import sys
#Usuario Actual
class AuthUser(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        abstract = True

#categoria
class Categorias(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre


#ingrediente enum?
class Ingredientes(models.Model):
    codigo = models.CharField(max_length=5)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True)
    cantidad = models.IntegerField()
    def __str__(self):
        return self.nombre


#producto

def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"users/{instance.categoria}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"

class Productos(models.Model):
    codigo = models.CharField(max_length=255, unique=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True)
    categoria = models.ForeignKey(Categorias, on_delete=CASCADE)
    precio = models.DecimalField(max_digits=9,decimal_places=2)
    ingredientes = models.ManyToManyField(Ingredientes)
    img_product = models.ImageField(("Img_product"), upload_to=upload_to, blank=True)
    def __str__(self):
        return self.nombre


#ventas
class Ventas(AuthUser):
    fecha_hora = models.DateTimeField(auto_now_add=True) #Guarda la fecha actual al momento de crearse
    total = models.DecimalField(max_digits=9,decimal_places=2)
    

#detalle_venta
class DetalleVenta(models.Model):
    id_venta = models.ForeignKey(Ventas, on_delete=CASCADE)
    id_producto = models.ForeignKey(Productos, on_delete=CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=9,decimal_places=2)

#ingrediente_producto
"""
fue remplazado por models.ManyToManyField(Ingredientes)
class IngredientesProducto(models.Model):
    id_ingrediente 
    id_producto
"""