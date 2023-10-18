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


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#     password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
#     password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#         # Saca los mensajes de ayuda
#         help_texts = {k:"" for k in fields}