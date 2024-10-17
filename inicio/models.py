from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    
    def __str__(self):
        return f"Nombre:{self.nombre},Apellido:{self.apellido},Edad:{self.edad}"