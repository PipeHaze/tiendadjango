from django.contrib import admin
from .models import Categoria, Producto

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug']
    prepopulated_fields = {'slug': ('nombre',)}

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'slug', 'precio',
                    'en_stock', 'creado', 'subido']
    list_filter = ['en_stock', 'activo']
    list_editable = ['precio', 'en_stock']
    prepopulated_fields = {'slug': ('titulo',)}