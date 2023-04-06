from django.shortcuts import render
from django.http.response import JsonResponse

from carritocompras.carritocompras import Carrito
from .models import Pedido, PedidoItem

# Create your views here.

def agregar(request):
    carrito = Carrito(request)
    if request.POST.get('action') == 'post':

        user_id = request.user.id
        pedido_key = request.POST.get('pedido_key')
        carritototal = Carrito.mostrar_precio()

        #comprobar si el pedido existe
        if Pedido.objects.filter(pedido_key = pedido_key).exists():
            pass
        else:
            pedido = Pedido.objects.create(user_id=user_id, nombre_completo = 'name', direccion1 = 'add1',
                                           direccion2 = 'add2',total_pagado = carritototal, pedido_key=pedido_key)
            pedido_id = pedido.pk

            for item in carrito:
                PedidoItem.objects.create(pedido_id=pedido_id, producto=item['producto'],precio=item['precio'], cantidad=item['qty'])

    response = JsonResponse({'success': 'Devolver algo'})
    return response
        
def payment_confirmation(data):
    Pedido.objects.filter(pedido_key=data).update(estado_factura=True)