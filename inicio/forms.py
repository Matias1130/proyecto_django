from django import forms

class EditarCliente(forms.Form):
    nombre = forms.CharField(max_length=20, required=True)
    apellido = forms.CharField(max_length=20, required=True)
    edad = forms.IntegerField(required=True, min_value=0)  
    email = forms.EmailField(max_length=254, required=True) 
    telefono = forms.CharField(max_length=20, required=True) 