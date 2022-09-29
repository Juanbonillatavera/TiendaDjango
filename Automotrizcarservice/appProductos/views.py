from asyncio.windows_events import NULL
from multiprocessing import context
from operator import concat
from django.shortcuts import render
from .models  import Producto,Carrito 


from django.http import JsonResponse
import json

# Create your views here.


def verProductos(request, id= NULL):

    if not id:
        listaProductos = Producto.objects.all()
        context = {
            'productos': listaProductos,
        }
        return render(request, 'productos/productos.html', context)
    else:
        id = int(id)
        regProducto = Producto.objects.get(id=id)
        context = {
            'producto': regProducto,
        }        
        return render(request, 'productos/unProducto.html', context)


def agregar (request, id= NULL):
    id = int(id)
    user = request.user
    regProducto = Producto.objects.get(id=id)
    existe= Carrito.objects.filter(cliente=user,producto = regProducto, estado ='carrito').exists()
    if existe:
        regCarrito = Carrito.objects.get(cliente=user,producto = regProducto, estado ='carrito')
        regCarrito.cantidad += 1
        regCarrito.save()
    else:
        regCarrito = Carrito(cliente = user, producto =regProducto, precio =regProducto.precio)
        regCarrito.save()   

    listaProductos = Producto.objects.all()
    context = {
            'productos': listaProductos,
        }
    return render(request, 'productos/productos.html', context)





def verCarrito(request):
    regUser= request.user
    carrito= Carrito.objects.filter(cliente=regUser, estado='carrito')
    context = {}
    if carrito:
        listaCarrito=[]
        total= 0
        for prod in carrito:

            unProducto={
            'cantidad': prod.cantidad,
            'icono': prod.producto.icono,
            'nombre': prod.producto.nombre,
            'precio': prod.producto.precio,
            'unidad' : prod.producto.unidad,
            'total' : int (prod.cantidad) * int(prod.producto.precio),
            'prodId' : prod.producto.id,
            'id' : prod.id,
            }

            listaCarrito.append(unProducto)
            total += unProducto['total']

        context={
            'carrito': listaCarrito,
            'subtotal': total,
            'iva': total * 0.19,
            'envio': 8000,
            'total' : total * 1.19 + 8000,
        }
    else:
        context['mensaje'] = 'El carrito está vacio.'
    return render(request,'productos/carrito.html', context)


def eliminarItemCarrito(request,id):

    regCarrito = Carrito.objects.get(id=id)
    regCarrito.estado = 'cancelado'

    regCarrito.save()

    return verCarrito(request)


def cambiarCantidad(request):
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH')=='XMLHttpRequest'
    

    if is_ajax:
        if request.method == 'POST':
            # TOMA LA DATA ENVIADA POR EL CLIENTE 
            data = json.load(request)
            id= data.get('id')
            cantidad= int(data.get('cantidad'))
            if cantidad > 0:
                #lee el registro y lo modifica
                regProducto = Carrito.objects.get(id=id)
                regProducto.cantidad = cantidad
                regProducto.save()
            
            return JsonResponse({'mensage': ' cantidad modificada a ' + str(cantidad)})

        return JsonResponse({'alarma': 'no se pudo modificar....'}, status=400)
    else:
        #return verCarrito(request)
        return JsonResponse({'alarma': 'no se pudo modificar....No AJAX'})