#Esto se maneja con rest_framework 

from rest_framework import viewsets
#Puedo importar modulos que no pertenezcan a un paquete pero que los use.
from .serializers import CategoriaSerializer, IngredienteSerializer, ProductoSerializer, VentaSerializer, DetalleVentaSerializer
from .models import Categorias, Ingredientes, Productos, Ventas, DetalleVenta
#Solucionar el problema de usuarios anonimos, puesto que genera un error no controlado
from rest_framework.permissions import IsAuthenticated

#Importamos el modulo de filtrado de django-rest-framework
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

#Aplicamos herencia CategoriasView, para que herede el CuerrentUser de esta forma pueda utilizar los atributos y metodos de viwsets.ModelViewSet y currentUser 
class CategoriasView(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriaSerializer

class IngredientesView(viewsets.ModelViewSet):
    queryset = Ingredientes.objects.all()
    serializer_class = IngredienteSerializer

class ProductosView(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductoSerializer
    search_fields = ['nombre'] 
    ordering_fields = ['categoria']
    ordering = ['categoria']

class VentasView(CurrentUser):
    queryset = Ventas.objects.all()
    serializer_class = VentaSerializer


class DetalleVentaView(viewsets.ModelViewSet):
    queryset = DetalleVenta.objects.all()        
    serializer_class = DetalleVentaSerializer
    search_fields = ['id_venta'] 
    ordering_fields = ['precio']
    ordering = ['id_venta']    


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