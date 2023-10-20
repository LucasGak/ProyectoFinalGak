from django.urls import path
from ProjectoFinal23 import views
from .views import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('cursos/', cursos, name="cursos"),
    path('profesores/', profesores, name="profesores"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('examenes/', examenes, name="examenes"),
    path('cursoFormulario/', views.cursoFormulario, name="cursoFormulario"),
    path('formulario_api/', views.formulario_api, name="formulario_api"),
    path('buscador_curso/', views.buscador_curso, name="buscador_curso"),
    path('acercadeMi/', views.acercadeMi, name="acercadeMi"),
    path('leerProfesores', views.leerProfesores, name = "LeerProfesores"),
    path('leerEstudiantes', views.leerEstudiantes, name = "LeerEstudiantes"),
    path('eliminarProfesor/<int:profesor_id>/', views.eliminarProfesor, name="EliminarProfesor"),
    path('editarProfesor/<int:profesor_id>/', views.editarProfesor, name="EditarProfesor"),
    path('registroProfesores/', views.registroProfesores, name="registroProfesores"),
    path('curso/list', login_required(views.CursoList.as_view()), name='List'),
    path(r'^(?P<pk>\d+)$', login_required(views.CursoDetalle.as_view()), name='Detail'),
    path(r'^nuevo$', login_required(views.CursoCreacion.as_view()), name='New'),
    path(r'^editar/(?P<pk>\d+)$', login_required(views.CursoUpdate.as_view()), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', login_required(views.CursoDelete.as_view()), name='Delete'),
    path('login/', views.login_request, name="login"),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(template_name='ProjectoFinal23/logout.html'), name='logout'),
    path('editarPerfil/', views.editarPerfil, name="editarPerfil"),
    path('registroEstudiante/', views.registroEstudiante, name="registroEstudiante"),
]
