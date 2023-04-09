from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Producto
from carritocompras import carritocompras
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.    

def listado (request):
    producto = Producto.producto.filter(aprobado = True)
    return render(request,"app/listado.html", {'producto': producto})

def productodetalle(request, slug):
    producto = get_object_or_404(Producto, slug=slug, en_stock=True)
    return render(request, 'app/detalle.html', {'producto': producto})

def categoria_lista(request, categoria_slug=None): 
    categoria = get_object_or_404(Categoria, slug = categoria_slug)
    productos = Producto.objects.filter(categoria = categoria)
    return render(request,'app/categorias.html', {'categoria': categoria, 'productos': productos})

def agregarproducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.creado_por = request.user
            categoria_id = request.POST.get('categoria')
            # Asignar la categoría al producto
            producto.categoria_id = categoria_id
            producto.aprobado = False
            producto.save()
            messages.success(request, 'el producto se ha agregado, pero tiene que ser aprobado por el administrador')
            return redirect(to='tiendita:agregarproducto')
    else:
        form = ProductoForm()
    return render(request, 'app/agregarproducto.html', {'form': form})

@login_required
def productos_pendientes(request):
    productos = Producto.objects.filter(aprobado = False)
    return render(request,'app/productos_pendientes.html', {'productos': productos})

def aprobar_producto(request, pk):
    producto = get_object_or_404(Producto, pk = pk)
    producto.aprobado = True
    producto.save()
    return redirect('tiendita:productos_pendientes')

def rechazar_producto(request, pk):
    producto = get_object_or_404(Producto, pk = pk)
    producto.delete()
    return redirect('tiendita:productos_pendientes')
    