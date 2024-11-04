from django.db import models

class Medicamentos(models.Model):
    marca = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)
    precio = models.CharField(max_length=10)
    def __str__(self):
        return f'|Marca: {self.marca}| |Descripcion: {self.descripcion}| |Precio: ${self.precio} por caja'
    
class Perfumes(models.Model):
    marca = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)
    genero = models.CharField(max_length=10,default = 'Unisex')
    precio = models.CharField(max_length=10)
    def __str__(self):
        return f'|Marca: {self.marca}| |Descripcion: {self.descripcion}| Genero: {self.genero} |Precio: ${self.precio} por unidad.'


