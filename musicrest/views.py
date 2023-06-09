from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ProductoSerializer, CategoriaSerializer,UserCreateSerializer, UserSerializer
from tiendita.models import Producto, Categoria
from account.models import UserBase
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class UserCreateViewSet(viewsets.ModelViewSet):
    queryset = UserBase.objects.all()
    serializer_class = UserCreateSerializer

class UserEnterViewSet(viewsets.ModelViewSet):
    queryset = UserBase.objects.all()
    serializer_class = UserSerializer

@api_view(['POST'])
def postProducto(request):
    data = request.data
    producto = Producto.objects.create(
        body = data['body']
    )
    serializer = ProductoSerializer(producto, many=False)
    return Response(serializer.data)
