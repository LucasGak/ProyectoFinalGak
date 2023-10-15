from django.shortcuts import render
from .models import *
from ProjectoFinal23.forms import BuscaCursoForm, CursoFormulario, ProfesorFormulario
# from django.views.generic import ListView
# from django.views.generic.detail import DetailView
# from django.urls import reverse_lazy
# from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


def inicio(request):

    return render(request, "ProjectoFinal23/index.html")

def cursos(request):

    return render(request, "ProjectoFinal23/cursos.html")

def profesores(request):

    return render(request, "ProjectoFinal23/profesores.html")

def estudiantes(request):

    return render(request, "ProjectoFinal23/estudiantes.html")

def entregables(request):

    return render(request, "ProjectoFinal23/entregables.html")

def cursoFormulario(request):
      
      if request.method == 'POST':
      
            curso =  Curso(nombre=request.POST['curso'], camada=request.POST['camada'])
 
            curso.save()
 
            return render(request, "ProjectoFinal23/padre.html")
 
      return render(request,"ProjectoFinal23/cursoFormulario.html")

def formulario_api(request):
    if request.method == "POST":
        
        miFormulario = CursoFormulario(request.POST) 

        if miFormulario.is_valid():
        
            informacion = miFormulario.cleaned_data
        
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
        
            curso.save()
            
            profesor = Profesor(nombre=informacion["profesor"])

            profesor.save()

            return render(request, "ProjectoFinal23/padre.html")

    else:
        miFormulario = CursoFormulario()

    return render(request, "ProjectoFinal23/formulario_api.html", {"miFormulario": miFormulario})

def profesores(request):
    
    if request.method == 'POST':

        miFormulario = ProfesorFormulario(request.POST) #aqui me llega toda la informacion del html

        print(miFormulario)

        if miFormulario.is_valid: #Si paso la validacion de Django
            informacion = miFormulario.cleaned_data

            profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
            email=informacion['email'], profesion=informacion['profesion'])
            
            profesor.save()

            return render(request, "ProjectoFinal23/padre.html") #vuelvo al inicio o donde quieran
        
    else:
        miFormulario=ProfesorFormulario() #Formulario vacio para construir el html
    
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

def leerProfesores(request):
    profesores = Profesor.objects.all() #trae todos los profesores

    contexto = {"profesores":profesores}

    return render(request, "ProjectoFinal23/leerProfesores.html",contexto)

def eliminarProfesor(request, profesor_id):
 
    profesor = Profesor.objects.get(id=int(profesor_id))
    profesor.delete()
 
    # vuelvo al menú
    profesores = Profesor.objects.all()  # trae todos los profesores
 
    contexto = {"profesores": profesores}
 
    return render(request, "ProjectoFinal23/leerProfesores.html", contexto)

def editarProfesor(request, profesor_id):
    #Si es metodo POST hago lo mismo que el agregar
    if request.method== 'POST':

        miFormulario = ProfesorFormulario(request.POST) #Aca llega la informacion del HTML

        if miFormulario.is_valid(): #Si paso la validacion de Django

            informacion = miFormulario.cleaned_data

            profesor = Profesor.objects.get(id=(profesor_id))
            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']
            profesor.save()

            return render(request, "ProjectoFinal23/padre.html") #Vuelvo al inicio
    
    else:
        profesor = Profesor.objects.get(id=(profesor_id))
        miFormulario= ProfesorFormulario(initial={'nombre': profesor.nombre, 'apellido':profesor.apellido, 'email':profesor.email, 'profesion':profesor.profesion})

    #HTML que permite editar
    return render(request, "ProjectoFinal23/formulario_api.html", {"miFormulario":miFormulario, "profesor_id":profesor_id})

# class CursoList(ListView):
#     model=Curso
#     template_name = "ProjectoFinal23/cursos_list.html"

# class CursoDetalle(DetailView):
#     model=Curso
#     template_name = "ProjectoFinal23/curso_detalle.html"

# class CursoCreacion(CreateView):
#     model=Curso
#     success_url="ProjectoFinal23/curso/list"
#     fields = ['nombre','camada']

# class CursoUpdate(UpdateView):
#     model=Curso
#     success_url="ProjectoFinal23/curso/list"
#     fields=['nombre','camada']

# class CursoDelete(DeleteView):
#     model=Curso
#     success_url="ProjectoFinal23/curso/list"

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

                return render(request,"ProjectoFinal23/padre.html", {"Mensaje":"ERROR, FORMULARIO ERRONEO"} )
        
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

def registroProfesores(request):
    
    if request.method == 'POST':

        miFormulario = ProfesorFormulario(request.POST) #aqui me llega toda la informacion del html

        print(miFormulario)

        if miFormulario.is_valid: #Si paso la validacion de Django
            informacion = miFormulario.cleaned_data

            profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
            email=informacion['email'], profesion=informacion['profesion'])
            
            profesor.save()

            return render(request, "ProjectoFinal23/padre.html") #vuelvo al inicio o donde quieran
        
    else:
        miFormulario=ProfesorFormulario() #Formulario vacio para construir el html
    
    return render(request, "ProjectoFinal23/registroProfesores.html", {"miFormulario":miFormulario})