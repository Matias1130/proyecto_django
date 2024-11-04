from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.CharField(max_length=20,default='default@example.com')
    telefono = models.IntegerField(default=0)
    edad = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad},Telefono: {self.telefono}, Email: {self.email}"

