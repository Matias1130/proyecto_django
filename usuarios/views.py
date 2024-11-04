from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm ,UserChangeForm 
from django.contrib.auth import authenticate,login as django_login
from usuarios.forms import FormularioUsuario,FormularioParaEdicionDePerfil,FormularioCambioContraseña
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import DatosExtra


def perfil(request):
    return render(request, 'usuarios/perfil_usuario.html', {'usuario': request.user})

def login (request):
    
    formulario = AuthenticationForm()
    
    if request.method == "POST":
        formulario = AuthenticationForm(request,data=request.POST)
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password')
            
            usuario = authenticate(username = nombre_usuario,password=password)
            
            django_login(request,usuario)
            
            DatosExtra.objects.get_or_create(user=usuario)
            
            return redirect('index')
    
    return render(request,'usuarios/login.html', {'form': formulario} )

def registrarse (request):
    
    formulario = FormularioUsuario()
    
    if request.method == "POST":
        
        formulario=FormularioUsuario(request.POST)
        
        if formulario.is_valid():
            
            formulario.save()
            
            return redirect('usuarios:login')
        
        
    return render(request,'usuarios/registrarse.html',{'form':formulario})

@login_required
def EditarUsuario(request):
    
    datos_extra = request.user.datosextra
    
    formulario = FormularioParaEdicionDePerfil(instance=request.user,initial={'avatar':datos_extra.avatar}) 
    
    if request.method == "POST":
        formulario = FormularioParaEdicionDePerfil(request.POST,request.FILES,instance=request.user) 
        if formulario.is_valid():
            new_avatar = formulario.cleaned_data.get('avatar')
            datos_extra.avatar = new_avatar if new_avatar else datos_extra.avatar
            datos_extra.save()
            formulario.save()
            
            return redirect('index')

    return render(request,'usuarios/editar_perfil.html' , {'form': formulario})

class CambiarClave(LoginRequiredMixin,PasswordChangeView):
    form_class = FormularioCambioContraseña
    template_name = 'usuarios/cambio_clave.html'
    success_url = reverse_lazy('usuarios:editar_perfil')
    
@login_required
def perfil_usuario(request):
    usuario = request.user
    context = {
        'usuario': usuario,
    }
    return render(request, 'perfil_usuario.html', context)