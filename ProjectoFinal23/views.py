from django.shortcuts import render
from .models import *
from ProjectoFinal23.forms import BuscaCursoForm, CursoFormulario, ProfesorFormulario


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
