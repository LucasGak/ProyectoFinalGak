from django import forms



class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()
    profesor=forms.CharField()

class BuscaCursoForm(forms.Form):
    curso = forms.CharField()

class ProfesorFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)

class EstudianteFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()

# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#     password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
#     password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#         # Saca los mensajes de ayuda
#         help_texts = {k:"" for k in fields}