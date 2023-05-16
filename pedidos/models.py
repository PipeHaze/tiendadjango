from django.db import models
from decimal import Decimal
from django.conf import settings

from tiendita.models import Producto

# Create your models here.

class Pedido(models.Model): #tabla venta
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pedido_user')
    nombre_completo = models.CharField(max_length=50)
    direccion1 = models.CharField(max_length=250)
    direccion2 = models.CharField(max_length=250)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    total_pagado = models.DecimalField(max_digits=7, decimal_places=3)
    pedido_key = models.CharField(max_length=200)
    estado_factura = models.BooleanField(default=False)

    class Meta:
        ordering = ('-creado',)

    def __str__(self):
        return str(self.creado)
    
class PedidoItem(models.Model): #detalle venta pero no quiero cambiar los datos de todas las tablas
    pedido = models.ForeignKey(Pedido,
                              related_name='items',
                              on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,
                                 related_name='pedido_items',
                                 on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=7, decimal_places=3)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)