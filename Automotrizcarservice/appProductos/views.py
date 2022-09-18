from asyncio.windows_events import NULL
from multiprocessing import context
from django.shortcuts import render
from .models  import Producto
# Create your views here.


def verProductos(request, id=NULL):
    if not id:
        listaProductos=Producto.objects.all()
        context={
            'productos':listaProductos,
        }
        return render(request,'productos/productos.html',context)