from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CursoFormulario(forms.Form):
    curso = forms.CharField()
    comision = forms.IntegerField()
    profesor=forms.CharField()

class BuscaCursoForm(forms.Form):
    curso = forms.CharField()

class ProfesorFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    especialidad= forms.CharField(max_length=30)

class EstudianteFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()

class ExamenesFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    FechaDeEntrega=forms.DateField()
    entregado=forms.BooleanField()
    
class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts = {k:"" for k in fields}

