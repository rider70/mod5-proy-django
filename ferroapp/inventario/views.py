from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .forms import ProductoForm 
from .serializers import CategoriaSerializer
from .serializers import ClienteSerializer
from .serializers import ProductoSerializer
from .models import Categoria
from .models import Cliente
from .models import Producto


def index(reQuest):
    return HttpResponse('hola mundo')

def productoFormView(reQuest):
    form = ProductoForm(reQuest.POST)

    if form.is_valid():
        form.save()
    return render(reQuest, "form_productos.html",{"form":form})

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

@api_view(["GET"])
def cliente_contador(request):
    """
    Cantidad de clientes en el modelo cliente
    """
    #logger.info("Cantidad cliente mostrada correctamente")
    try:
        cantidad = Cliente.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

# Create your views here.
