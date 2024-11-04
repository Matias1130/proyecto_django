from django.http import HttpResponse
from django.template import Template , Context
from django.shortcuts import render,redirect,get_object_or_404
from inicio.models import Cliente
from inicio.forms import EditarCliente
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request,'index.html')

def registro(request):
    return render(request, "registro.html")

def lista (request):
    return render(request,"lista.html")

@login_required
def registro_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        edad = request.POST.get('edad')
        email= request.POST.get('email')
        telefono = request.POST.get('telefono')

        if nombre and apellido and edad:
            Cliente.objects.create(nombre=nombre, apellido=apellido, edad=edad, email=email,telefono=telefono)
            return redirect('lista') 

    return render(request, 'registro.html')  

@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})


def ver_cliente(request,id):
    cliente = Cliente.objects.get(id=id)
    return render(request,'ver_clientes.html',{'cliente': cliente } )


def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return redirect('lista')


def editar_cliente(request,id):
    cliente = Cliente.objects.get(id=id)
    
    formulario = EditarCliente()
    
    if request.method == "POST":
        formulario = EditarCliente(request.POST)
        if formulario.is_valid():
            cliente.nombre = formulario.cleaned_data.get('nombre')
            cliente.apellido = formulario.cleaned_data.get('apellido')
            cliente.edad = formulario.cleaned_data.get('edad')
            cliente.email = formulario.cleaned_data.get('email')
            cliente.telefono = formulario.cleaned_data.get('telefono')
                        
            cliente.save()
            return redirect('lista')
    return render(request, 'editar_cliente.html', {'cliente':cliente, 'form':formulario})
