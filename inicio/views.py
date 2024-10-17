from django.http import HttpResponse
from django.template import Template , Context
from django.shortcuts import render,redirect
from inicio.models import Cliente
def inicio(request):
    return render(request,'index.html')

def registro(request):
    return render(request, "registro.html")

def lista (request):
    return render(request,"lista.html")

def registro_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        edad = request.POST.get('edad')

        if nombre and apellido and edad:
            Cliente.objects.create(nombre=nombre, apellido=apellido, edad=edad)
            return redirect('lista') 

    return render(request, 'registro.html')  


def lista_clientes(request):
    query = request.GET.get('nombre', '')
    clientes = Cliente.objects.filter(nombre__icontains=query)
    return render(request, 'lista.html', {'clientes': clientes})

