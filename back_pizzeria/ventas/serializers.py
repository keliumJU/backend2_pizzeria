#funciones principales que van a interactuar con nuestro modelo(API)

from rest_framework import serializers
from .models import Categorias, Ingredientes, Productos, Ventas, DetalleVenta

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        #Los campos que deseo serializar ... "__all__" es para todos los datos
        #sin embargo tambien puedo colocar solo los que necesito como nombre ...
        fields = "__all__"
        #Esta linea nos permite ocultar el campo de usuario actual
        #porque se supone que todas las acciones realizadas seran con dicho usuario.
    usuario = serializers.HiddenField(default = serializers.CurrentUserDefault())

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredientes
        fields = "__all__"

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = "__all__"
        #fields = ["avatar"]
    """def save(self, *args, **kwargs):
        if self.instance.avatar:
            self.instance.avatar.delete()
        return super().save(*args, **kwargs)
    """
class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ventas
        fields = "__all__"

    #dejamos oculto el usuario que realizo x venta
    usuario = serializers.HiddenField(default = serializers.CurrentUserDefault())

class DetalleVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleVenta
        fields = "__all__"    
    usuario = serializers.HiddenField(default = serializers.CurrentUserDefault())

"""
class CategoriaSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    nombre = serializers.CharField()

    #La funcion create del API
    def create(self, data):
        categoria = Categorias()
        categoria.nombre = data.get('nombre')
        categoria.save()
        return categoria
"""
    

