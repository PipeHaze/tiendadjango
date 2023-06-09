from django.urls import path, include
from rest_framework import routers
from musicrest import views
from . import views

app_name = 'music_rest'

router = routers.DefaultRouter()
router.register(r'producto',views.ProductoViewSet)
router.register(r'categoria',views.CategoriaViewSet)
router.register(r'usuarios',views.UserCreateViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('post/', views.postProducto)


]