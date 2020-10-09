from django.shortcuts import render
from django.http import HttpResponse

def saludo(request, nombre):
    return HttpResponse("hola desde gestion de transaccion " + nombre) 