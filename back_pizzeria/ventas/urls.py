from django.urls import path
from .views import CategoriasView, ProductosView, VentasView, DetalleVentaView, getLastVenta, IngredientesView, RegistrarVenta, getLastVenta
from . import views

urlpatterns = [
    #Habilito las acciones del viewset
    #es mejor utilizar sustativos en luagar de verbos en los nombres de las rutas
    path('registrarVenta/', # urls list all and create new one
        views.RegistrarVenta.as_view(),
        name='RegistrarVenta'
    ),
    path('categorias/', CategoriasView.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('last_venta/', getLastVenta.as_view()),
    #Habilitamos los metodos get id, put y delete en la ruta del API    
    path('categorias/<int:pk>', CategoriasView.as_view({ #El <int:pk> es la llave primaria obligatoria que exige rest_framework para buscar un registro en particular(convención)
        'get': 'retrieve', #me retorna un registro filtrado por la primary key
        'put': 'update',
        'delete': 'destroy'
    })),
    path('productos/', ProductosView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('productos/<int:pk>', ProductosView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
        path('ventas/', VentasView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('ventas/<int:pk>', VentasView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
        path('detalleventa/', DetalleVentaView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('detalleventa/<int:pk>', DetalleVentaView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
        path('ingredientes/', IngredientesView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('ingredientes/<int:pk>', IngredientesView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))
    
]