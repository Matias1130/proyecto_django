from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from medicamentos.models import Medicamentos, Perfumes
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



class CrearMedicamento(LoginRequiredMixin,CreateView):
    model = Medicamentos
    template_name = "medicamentos/crear_medicamento.html"
    success_url = reverse_lazy('medicamentos:listado_medicamentos')
    fields = ['marca', 'descripcion', 'precio']


class ListadoMedicamentos(LoginRequiredMixin,ListView):
    model = Medicamentos
    template_name = "medicamentos/lista_medicamentos.html"
    context_object_name = 'medicamentos'
    

class VerMedicamentos(LoginRequiredMixin,DetailView):
    model = Medicamentos
    template_name = "medicamentos/ver_medicamentos.html"


class EditarMedicamentos(LoginRequiredMixin,UpdateView):
    model = Medicamentos
    template_name = "medicamentos/editar_medicamentos.html"
    success_url = reverse_lazy('medicamentos:listado_medicamentos')
    fields = ['marca', 'descripcion', 'precio']



class EliminarMedicamento(LoginRequiredMixin,DeleteView):
    model = Medicamentos
    template_name = "medicamentos/eliminar_medicamento.html"
    success_url = reverse_lazy('medicamentos:listado_medicamentos')




class CrearPerfumes(LoginRequiredMixin,CreateView):
    model = Perfumes
    template_name = "medicamentos/crear_perfumes.html"  
    success_url = reverse_lazy('medicamentos:listado_perfumes')  
    fields = ['marca', 'descripcion','genero', 'precio']


class ListadoPerfumes(LoginRequiredMixin,ListView):
    model = Perfumes
    template_name = "medicamentos/lista_perfumes.html"  
    context_object_name = 'perfumes'  

class VerPerfumes(LoginRequiredMixin,DetailView):
    model = Perfumes
    template_name = "medicamentos/ver_perfumes.html"
    
    
class EditarPerfumes(LoginRequiredMixin,UpdateView):
    model = Perfumes
    template_name = "medicamentos/editar_perfumes.html"
    success_url = reverse_lazy('medicamentos:listado_perfumes')
    fields = ['marca', 'descripcion','genero', 'precio']


class EliminarPerfume(LoginRequiredMixin,DeleteView):
    model = Perfumes
    template_name = "medicamentos/eliminar_perfume.html"
    success_url = reverse_lazy('medicamentos:listado_perfumes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['perfume'] = self.get_object() 
        return context