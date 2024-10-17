from django.urls import path
from inicio.views import inicio, registro_cliente, lista_clientes

urlpatterns = [
    path('', inicio, name="index"),  # Ruta para la página de inicio
    path('registro/', registro_cliente, name='registro'),  # Ruta para el registro
    path('lista/', lista_clientes, name='lista'),  # Ruta para la lista de clientes
]
