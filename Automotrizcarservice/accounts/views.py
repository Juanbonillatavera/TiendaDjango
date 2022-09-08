from ast import Return
from django.shortcuts import render

# Create your views here.

def registrarse(request):
    return render(request, 'registro.html')