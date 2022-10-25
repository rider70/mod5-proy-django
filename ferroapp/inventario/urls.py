from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from .models import Categoria
from .models import Cliente
from .models import Producto
from . import views

router = DefaultRouter()
router.register(r"categorias", views.CategoriaViewSet)
router.register(r"cliente", views.ClienteViewSet)
router.register(r"producto", views.ProductoViewSet)


urlpatterns = [
    #path("",views.index, name="index"),
    #path('productos/', views.productoFormView, name='productos'),
    path('cliente/cantidad', views.cliente_contador),
    path('', include(router.urls)),
]