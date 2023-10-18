from django.db import models


#Creados los modelos curso, estudiante, profesor y entregable

class Curso(models.Model):

    nombre=models.CharField(max_length=40)
    camada=models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Camada {self.camada}"

    
class Estudiante(models.Model):
    nombre= models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    curso=models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Curso: {self.curso}"

class Profesor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    profesion=models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Profesion: {self.profesion}"

class Entregable(models.Model):
    nombre=models.CharField(max_length=30)
    FechaDeEntrega=models.DateField()
    entregado=models.BooleanField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Fecha De Entrega: {self.FechaDeEntrega} - Entregado: {self.entregado}"

