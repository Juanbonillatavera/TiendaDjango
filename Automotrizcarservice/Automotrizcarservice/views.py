
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


def verServicios(request):
    return render(request, 'servicios.html')



def verInformacionEmpresa(request):
    return render(request, 'quienes_somos.html')


def verContactenos(request):
    return render(request,'contactenos.html')
