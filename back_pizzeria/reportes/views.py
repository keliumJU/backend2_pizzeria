from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def reportes(request):
    return HttpResponse("hola desde gestion de transaccion ")
