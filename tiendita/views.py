from django.shortcuts import render, get_object_or_404
from .models import Categoria, Producto
from carritocompras import carritocompras
# Create your views here.    

def listado (request):
    producto = Producto.producto.all()
    return render(request,"app/listado.html", {'producto': producto})

def productodetalle(request, slug):
    producto = get_object_or_404(Producto, slug=slug, en_stock=True)
    return render(request, 'app/detalle.html', {'producto': producto})

def categoria_lista(request, categoria_slug=None): 
    categoria = get_object_or_404(Categoria, slug = categoria_slug)
    productos = Producto.objects.filter(categoria = categoria)
    return render(request,'app/categorias.html', {'categoria': categoria, 'productos': productos})