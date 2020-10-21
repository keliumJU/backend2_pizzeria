#funciones principales que van a interactuar con nuestro modelo(API)

from rest_framework import serializers
from .models import Compras, Proveedores, DetalleCompra

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compras
        fields = "__all__"
    #dejamos oculto el cliente que realizo x compra
    usuario = serializers.HiddenField(default = serializers.CurrentUserDefault())

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedores
        fields = "__all__"

class DetalleCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleCompra
        fields = "__all__"
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
    

