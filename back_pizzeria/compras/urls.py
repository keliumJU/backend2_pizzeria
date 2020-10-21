from django.urls import path
from .views import ComprasView, ProveedoresView, DetalleCompraView

urlpatterns = [
    #Habilito las acciones del viewset
    #es mejor utilizar sustativos en luagar de verbos en los nombres de las rutas
    path('compraproduct/', ComprasView.as_view({
        'get': 'list',
        'post': 'create',
    })),
    #Habilitamos los metodos get id, put y delete en la ruta del API    
    path('compraproduct/<int:pk>', ComprasView.as_view({ #El <int:pk> es la llave primaria obligatoria que exige rest_framework para buscar un registro en particular(convención)
        'get': 'retrieve', #me retorna un registro filtrado por la primary key
        'put': 'update',
        'delete': 'destroy'
    })),
    path('proveedores/', ProveedoresView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('proveedores/<int:pk>', ProveedoresView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
        path('detallecompra/', DetalleCompraView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('detallecompra/<int:pk>', DetalleCompraView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))
    
]