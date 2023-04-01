from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static
from .views import listado, productodetalle

app_name = 'tiendita'


urlpatterns = [
    path('',listado,name="listado"),
    path('item/<slug:slug>/', views.productodetalle,name="producto_detalle"),
    path('search/<slug:categoria_slug>/', views.categoria_lista, name='categoria_lista'),

]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)