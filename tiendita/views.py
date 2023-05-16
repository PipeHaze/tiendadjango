from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Producto
from carritocompras import carritocompras
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
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
            # Obtener el objeto del formulario sin guardarlo en la base de datos
            producto = form.save(commit=False)           
            # Asignar el usuario actual como creador del producto
            producto.creado_por = request.user
            # Obtener el ID de la categoría seleccionada en el formulario
            categoria_id = request.POST.get('categoria')           
            # Asignar la categoría al producto
            producto.categoria_id = categoria_id
            # Marcar el producto como no aprobado
            producto.aprobado = False
            
            # Guardar el producto en la base de datos
            producto.save()
            # Mostrar un mensaje de éxito al usuario
            messages.success(request, 'El producto se ha agregado, pero tiene que ser aprobado por el administrador')
            
            # Redirigir al usuario al formulario de agregar producto para agregar más productos
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


def buscar_pendientes(request):
    queryset = request.GET.get("buscar")#este es el nombre que sale el el buscador de la pagina productos pendientes.
    productos = Producto.objects.filter(aprobado=False)
    
    if queryset:
        productos = Producto.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()
    
    return render(request, 'app/productos_pendientes.html', {'productos': productos})
    