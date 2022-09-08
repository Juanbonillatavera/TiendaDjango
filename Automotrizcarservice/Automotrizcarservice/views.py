
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


def verServicios(request):
    return render(request, 'servicios.html')

def verInfomacionContacto(request):
    return render(request, 'contactenos.html')


def verInformacionEmpresa(request):
    return render(request, 'quienes_somos.html')
