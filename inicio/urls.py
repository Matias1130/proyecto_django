from django.urls import path
from inicio.views import inicio, registro_cliente, lista_clientes, ver_cliente,eliminar_cliente,editar_cliente


urlpatterns = [
    path('', inicio, name="index"), 
    path('registro/', registro_cliente, name='registro'),  
    path('lista_clientes/', lista_clientes, name='lista'), 
    path('ver-clientes/<int:id>/', ver_cliente,name='ver_clientes'),
    path('eliminar/<int:id>/', eliminar_cliente, name='eliminar_cliente'),
    path('editar_cliente/<int:id>/',editar_cliente,name='editar_cliente'),
    
]
