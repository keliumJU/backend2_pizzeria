"""back_pizzeria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

#Endpoint de login
from rest_framework_jwt.views import obtain_jwt_token
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transaccion/', include('gestion_transaccion.urls')),
    path('compras/', include('compras.urls')),
    path('ventas/', include('ventas.urls')),
    path('auth/', obtain_jwt_token) #Al loguearnos en esta ruta generamos un token de autenticacion que dura 5 min aprox
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)