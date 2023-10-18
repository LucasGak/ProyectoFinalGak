from django.db import models


#Creados los modelos curso, estudiante, profesor y entregable

class Curso(models.Model):

    nombre=models.CharField(max_length=40)
    profesor=models.CharField(max_length=40)
    comision=models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Comision: {self.comision}"

    
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
    especialidad=models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Especialidad: {self.especialidad}"

class Examenes(models.Model):
    nombre=models.CharField(max_length=30)
    FechaDeEntrega=models.DateField()
    entregado=models.BooleanField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Fecha De Entrega: {self.FechaDeEntrega} - Entregado: {self.entregado}"