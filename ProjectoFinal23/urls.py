from django.urls import path
from ProjectoFinal23 import views
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('cursos/', cursos, name="cursos"),
    path('profesores/', profesores, name="profesores"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('entregables/', entregables, name="entregables"),
    path('cursoFormulario/', views.cursoFormulario, name="cursoFormulario"),
    path('formulario_api/', views.formulario_api, name="formulario_api"),
    path('buscador_curso/', views.buscador_curso, name="buscador_curso"),
    path('leerProfesores', views.leerProfesores, name = "LeerProfesores"),
    path('eliminarProfesor/<int:profesor_id>/', views.eliminarProfesor, name="EliminarProfesor"),
    path('editarProfesor/<int:profesor_id>/', views.editarProfesor, name="EditarProfesor"),
    path('registroProfesores/', views.registroProfesores, name="registroProfesores"),
    path('curso/list', views.CursoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.CursoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='Delete'),
    path('login/', views.login_request, name="login"),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(template_name='ProjectoFinal23/logout.html'), name='logout'),
    path('editarPerfil/', views.editarPerfil, name="editarPerfil"),
    path('registroEstudiante/', views.registroEstudiante, name="registroEstudiante"),
]
