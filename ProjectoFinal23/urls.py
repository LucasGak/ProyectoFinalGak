from django.urls import path
from ProjectoFinal23 import views
from .views import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required, user_passes_test


def group_required(group):
    return user_passes_test(lambda u: u.groups.filter(name=group).exists()or u.is_superuser or u.is_staff)

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
    path('eliminarProfesor/<int:profesor_id>/', login_required(group_required('staff')(views.eliminarProfesor)), name="EliminarProfesor"),
    path('editarProfesor/<int:profesor_id>/', login_required(group_required('staff')(views.editarProfesor)), name="EditarProfesor"),
    path('registroProfesores/', views.registroProfesores, name="registroProfesores"),
    path('curso/list', login_required(views.CursoList.as_view()), name='List'),
    path('curso/<int:pk>', login_required(group_required('staff')(views.CursoDetalle.as_view())), name='Detail'),
    path('curso/nuevo', login_required(group_required('staff')(views.CursoCreacion.as_view())), name='New'),
    path('curso/editar/<int:pk>', login_required(group_required('staff')(views.CursoUpdate.as_view())), name='Edit'),
    path('curso/borrar/<int:pk>', login_required(group_required('superuser')(views.CursoDelete.as_view())), name='Delete'),
    path('login/', views.login_request, name="login"),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(template_name='ProjectoFinal23/logout.html'), name='logout'),
    path('editarPerfil/', views.editarPerfil, name="editarPerfil"),
    path('registroEstudiante/', views.registroEstudiante, name="registroEstudiante"),
    path('subirExamen/', views.subirExamenes, name='subirExamen'),
    path('profesorCreado/', views.profesor_creado, name='profesorCreado'),
    path('alumnoCreado/', views.alumno_creado, name='alumnoCreado'),
    path('usuarioCreado/', views.usuario_creado, name='usuarioCreado'),
    path('examenSubido.html', views.examen_subido, name='examenSubido'),
    path('cursoCreado', views.curso_creado, name='cursoCreado'),
]
