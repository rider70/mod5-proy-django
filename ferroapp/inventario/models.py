from django.db import models
from django.conf import settings

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class ProductUnits(models.TextChoices):
    UNITS = 'u', 'Unidades'
    KG = 'kg', 'Kilogramos'

class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True) 
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) 
    description = models.TextField()
    precio = models.DecimalField(decimal_places=2, max_digits=10)
    unidades = models.CharField(
        max_length=2,
        choices=ProductUnits.choices,
        default=ProductUnits.UNITS 
     )
    disponible = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Producto - %s" % self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    apellido = models.CharField(max_length=100, unique=True)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre +' '+ self.apellido

class EstadoOrden(models.TextChoices):
    NOPAGADO = 'nopagado', 'No Pagado'
    PAGADO = 'pagado', 'Pagado'

class Orden(models.Model):
    total = models.IntegerField(default=0)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) 
    fecha = models.DateField()
    vendedor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="inventario_orden_vendedor"
    )
    estado = models.CharField(
        max_length=10,
        choices=EstadoOrden.choices,
        default=EstadoOrden.NOPAGADO
    )

class OrdenProducto(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE) 
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE) 
    cantidad = models.IntegerField(default=0)
    precio = models.DecimalField(decimal_places=2, max_digits=10)

# Create your models here.
