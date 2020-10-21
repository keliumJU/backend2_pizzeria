from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField
#Importamos los modelos de categorias y el producto
from ventas.models import Categorias, Ingredientes
#colocar el atributo "unique=True" a los campos que lo necesiten(analizarlo)

#Usuario Actual
class AuthUser(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        abstract = True

#proveedor
class Proveedores(models.Model):
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    #Mostrar el nombre del provedor al listar los objetos de la clase proveedores en el api restful
    def __str__(self):
        return self.nombre

#compras
class Compras(AuthUser):
    id_proveedor = models.ForeignKey(Proveedores, on_delete=CASCADE)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    nro_factura = models.CharField(max_length=5)
    total = models.DecimalField(max_digits=9, decimal_places=2)
    def __str__(self):
        return self.nro_factura

  
#detalle_compra
#Esta clase utiliza modelos de la app ventas(ingredientes y categorias)
class DetalleCompra(models.Model):
    id_compra = models.ForeignKey(Compras, on_delete=CASCADE)
    id_ingrediente = models.ForeignKey(Ingredientes, on_delete=CASCADE) #se relaciona con la clase ingredientes de la app ventas
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    cantidad = models.IntegerField()
    id_categoria = models.ForeignKey(Categorias, on_delete=CASCADE) #posiblemente se relaciona con la app categorias
    def __str__(self):
        return self.id_compra
#ingredientes_producto --> se relaciona con la app ventas
#esta tabla puede ser ManyToManyField ... asesiorarme de la posible mejor manera ...
'''
class IngredientesProducto(models.Model):
    id_producto 
    id_ingrediente
'''