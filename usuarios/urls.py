from django.urls import path
from usuarios import views
from django.contrib.auth.views import  LogoutView


app_name= 'usuarios'


urlpatterns = [
    path('login/', views.login ,name='login'),
    path('registrarse/', views.registrarse ,name='registrarse'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'),name='logout'),
    path('perfil/editar', views.EditarUsuario, name='editar_perfil'),
    path('perfil/editar/clave', views.CambiarClave.as_view(), name='cambio_clave'),
    path('perfil/', views.perfil, name='perfil'),
]
