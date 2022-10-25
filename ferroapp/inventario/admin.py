from django.contrib import admin
from .models import Categoria
from .models import Producto
from .models import Cliente
from .models import Orden
from .models import OrdenProducto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio", "unidades")
    ordering = ["precio"]
    search_fields = ["nombre"]
    list_filter = ("disponible","precio")

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "direccion")

class OrdenAdmin(admin.ModelAdmin):
    list_display = ("total", "cliente", "fecha", "vendedor", "estado")

class OrdenProdAdmin(admin.ModelAdmin):
    list_display = ("orden", "producto", "cantidad", "precio")

admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Orden, OrdenAdmin)
admin.site.register(OrdenProducto, OrdenProdAdmin)

# Register your models here.
