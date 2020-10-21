#Esto se maneja con rest_framework 

from rest_framework import viewsets
#Puedo importar modulos que no pertenezcan a un paquete pero que los use.
from .serializers import CompraSerializer, ProveedorSerializer, DetalleCompraSerializer
from .models import Compras, Proveedores, DetalleCompra
#Solucionar el problema de usuarios anonimos, puesto que genera un error no controlado
from rest_framework.permissions import IsAuthenticated

#modulo de filtros, busquedas y paginacion en rest_framework django
from django_filters.rest_framework import DjangoFilterBackend


#Vista para filtrar los modelos de acuerdo al usuario actual
class CurrentUser(viewsets.ModelViewSet):
    def get_queryset(self):
        #Le asignamos a la variable usuario el usuario actual
        user = self.request.user
        #retornamos un filtro de los objetos en base al usuario actual
        return self.serializer_class.Meta.model.objects.filter(usuario=user)
    #permission_classes nos ayuda a controlar los usuarios Anonimos
    permission_classes = [IsAuthenticated]        

#Aplicamos herencia CategoriasView, para que herede el CuerrentUser de esta forma utilizar los atributos y metodos de viwsets.ModelViewSet y currentUser 

class ComprasView(CurrentUser):
    queryset = Compras.objects.all()
    serializer_class = CompraSerializer
    #limitamos las opciones de busqueda solo por nombre ... se puede por mas campos
    #search_fields = ['fecha_hora'] 
    search_fields = ['nro_factura'] 

    #limitamos las opciones de ordenamiento solo por nombre ... se puede por mas campos
    ordering_fields = ['fecha_hora']
    #Estipulamos un orden por defecto al listar los elementos del modelo ... 
    ordering = ['fecha_hora']
    
class ProveedoresView(viewsets.ModelViewSet):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedorSerializer

class DetalleCompraView(viewsets.ModelViewSet):
    queryset = DetalleCompra.objects.all()
    serializer_class = DetalleCompraSerializer
    search_fields = ['id_categoria'] 
    ordering_fields = ['id_compra']
    ordering = ['id_compra']
"""
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import CategoriaSerializer

class CategoriasView(APIView):
    def post(self, request):
        categoria_serializer = CategoriaSerializer(data=request.data)
    
        if categoria_serializer.is_valid():
            categoria_serializer.save()
            return Response(
                categoria_serializer.data, 
                status.HTTP_201_CREATED
                )
        else:
            return Response(
                categoria_serializer.errors,
                 status.HTTP_400_BAD_REQUEST
                 )
"""