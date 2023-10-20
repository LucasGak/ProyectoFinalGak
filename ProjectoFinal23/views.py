from django.shortcuts import render
from .models import *
from ProjectoFinal23.forms import BuscaCursoForm, CursoFormulario, ProfesorFormulario, EstudianteFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm



def inicio(request):

    return render(request, "ProjectoFinal23/index.html")

@login_required
def cursos(request):

    return render(request, "ProjectoFinal23/cursos.html")

@login_required
def profesores(request):

    return render(request, "ProjectoFinal23/profesores.html")

@login_required
def estudiantes(request):

    return render(request, "ProjectoFinal23/estudiantes.html")

@login_required
def examenes(request):
    examenes = Examenes.objects.all()

    contexto = {"examenes":examenes}

    return render(request, "ProjectoFinal23/examenes.html", contexto)

@login_required
def cursoFormulario(request):
      
      if request.method == 'POST':
      
            curso =  Curso(nombre=request.POST['curso'], comision=request.POST['comision'])
 
            curso.save()
 
            return render(request, "ProjectoFinal23/padre.html")
 
      return render(request,"ProjectoFinal23/formulario_api.html")

@login_required
def formulario_api(request):
    if request.method == "POST":
        
        miFormulario = CursoFormulario(request.POST) 

        if miFormulario.is_valid():
        
            informacion = miFormulario.cleaned_data
        
            curso = Curso(nombre=informacion["curso"], comision=informacion["comision"])
        
            curso.save()
            
            profesor = Profesor(nombre=informacion["profesor"])

            profesor.save()

            return render(request, "ProjectoFinal23/padre.html")

    else:
        miFormulario = CursoFormulario()

    return render(request, "ProjectoFinal23/formulario_api.html", {"miFormulario": miFormulario})

@login_required
def profesores(request):
    
    if request.method == 'POST':

        miFormulario = ProfesorFormulario(request.POST) 


        if miFormulario.is_valid: 
            informacion = miFormulario.cleaned_data

            profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
            email=informacion['email'], especialidad=informacion['especialidad'])
            
            profesor.save()

            return render(request, "ProjectoFinal23/padre.html") 
        
    else:
        miFormulario=ProfesorFormulario() 
    
    return render(request, "ProjectoFinal23/profesores.html", {"miFormulario":miFormulario})

def buscador_curso(request):
    if request.method == "POST":
        miFormulario = BuscaCursoForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])


            return render(request, "ProjectoFinal23/resultados_buscador.html", {"cursos": cursos})
    else:
        miFormulario = BuscaCursoForm()

    return render(request, "ProjectoFinal23/buscador_curso.html", {"miFormulario": miFormulario})

@login_required
def leerProfesores(request):
    profesores = Profesor.objects.all()

    contexto = {"profesores":profesores}

    return render(request, "ProjectoFinal23/leerProfesores.html",contexto)

@login_required
def leerEstudiantes(request):
    estudiantes = Estudiante.objects.all()

    contexto = {"estudiantes":estudiantes}

    return render(request, "ProjectoFinal23/leerEstudiantes.html",contexto)

def eliminarProfesor(request, profesor_id):
 
    profesor = Profesor.objects.get(id=int(profesor_id))
    profesor.delete()
 

    profesores = Profesor.objects.all() 
 
    contexto = {"profesores": profesores}
 
    return render(request, "ProjectoFinal23/leerProfesores.html", contexto)

def editarProfesor(request, profesor_id):

    if request.method== 'POST':

        miFormulario = ProfesorFormulario(request.POST) 

        if miFormulario.is_valid(): 

            informacion = miFormulario.cleaned_data

            profesor = Profesor.objects.get(id=(profesor_id))
            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.especialidad = informacion['especialidad']
            profesor.save()

            return render(request, "ProjectoFinal23/padre.html") 
    
    else:
        profesor = Profesor.objects.get(id=(profesor_id))
        miFormulario= ProfesorFormulario(initial={'nombre': profesor.nombre, 'apellido':profesor.apellido, 'email':profesor.email, 'especialidad':profesor.especialidad})


    return render(request, "ProjectoFinal23/formulario_api.html", {"miFormulario":miFormulario, "profesor_id":profesor_id})


class CursoList(ListView):
     model=Curso
     template_name = "ProjectoFinal23/cursos_list.html"


class CursoDetalle(DetailView):
    model=Curso
    template_name = "ProjectoFinal23/curso_detalle.html"


class CursoCreacion(CreateView):
    model=Curso
    success_url="/ProjectoFinal23/curso/list"
    fields = ['nombre','comision']


class CursoUpdate(UpdateView):
    model=Curso
    success_url="/ProjectoFinal23/curso/list"
    fields=['nombre','comision']


class CursoDelete(DeleteView):
     model=Curso
     success_url="/ProjectoFinal23/curso/list"


def login_request(request):

    if request.method == "POST":
        form=AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=password)

            if usuario is not None:
                login(request, user)

                return render(request,"ProjectoFinal23/padre.html", {"Mensaje":f"Bienvenido {usuario}"} )
            else:

                form = AuthenticationForm()
                return render(request,"ProjectoFinal23/login.html", {"Mensaje":"ERROR, datos incorrectos", 'form':form} )
            
        else:

                return render(request,"ProjectoFinal23/padre.html", {"Mensaje":"Nombre de usuario inexistente, o clave incorrecta."} )
        
    form = AuthenticationForm()

    return render(request,"ProjectoFinal23/login.html", {'form':form} )

def register(request):
    
    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render (request, "ProjectoFinal23/padre.html", {"mensaje": "Usuario Creado" })
        
    else:
        form = UserCreationForm()

    return render(request, "ProjectoFinal23/registro.html", {'form':form})

@login_required
def registroProfesores(request):
    
    if request.method == 'POST':

        miFormulario = ProfesorFormulario(request.POST) 

        if miFormulario.is_valid(): 
            informacion = miFormulario.cleaned_data

            profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
            email=informacion['email'], especialidad=informacion['especialidad'])
            
            profesor.save()

            return render(request, "ProjectoFinal23/padre.html") 
        
    else:
        miFormulario=ProfesorFormulario() 
    
    return render(request, "ProjectoFinal23/formulario_api.html", {"miFormulario":miFormulario})

@login_required
def registroEstudiante(request):
    
    if request.method == 'POST':

        miFormulario = EstudianteFormulario(request.POST)


        if miFormulario.is_valid(): 
            informacion = miFormulario.cleaned_data

            estudiante = Estudiante(nombre=informacion['nombre'], apellido=informacion['apellido'],
            email=informacion['email'])
            
            estudiante.save()

            return render(request, "ProjectoFinal23/padre.html") 
        
    else:
        miFormulario=EstudianteFormulario()
    
    return render(request, "ProjectoFinal23/formulario_api.html", {"miFormulario":miFormulario})

@login_required
def editarPerfil(request):

    usuario = request.user
    
    if request.method == 'POST':
        
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
            if informacion["password1"] != informacion["password2"]:
                datos = {'first_name': usuario.first_name,'email': usuario.email}
                miFormulario = UserEditForm(initial=datos)

            else:
                usuario.email = informacion['email']
                if informacion["password1"]:
                    usuario.set_password(informacion["password1"])
                usuario.last_name = informacion['last_name']
                usuario.first_name = informacion['first_name']
                usuario.save()

            return render(request, "ProjectoFinal23/cambioPassword.html")
        
    else:
        datos = {'first_name': usuario.first_name, 'last_name':usuario.last_name, 'email': usuario.email, }
        miFormulario= UserEditForm(initial=datos)

    return render(request, "ProjectoFinal23/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})


def acercadeMi(request):

    return render(request, "ProjectoFinal23/acercadeMi.html")
