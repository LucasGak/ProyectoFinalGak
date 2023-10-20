# PROYECTO FINAL - CURSO PYTHON CODERHOUSE - LUCAS GAK COMISION 47770

# Nombre del proyecto
    SMART TRAINING

# Version
    0.1

## Descripcion del proyecto

Es una pagina web en la que alumnos que quieren entrar a esta academia de educacion fisica orientada a distintas disciplinas se puede registrar y elegir un curso en el momento que se registran.

Aca voy a ir dejando data de lo que se hizo hasta ahora para seguir al dia siguiente
- Arme una web Django con patrón MVT
- Hice la herencia de HTML con el index y padre, y tambien con otros
- Un formulario para registrar cursos en la BD tanto en HTML como usando la API de Django
- Agregue el buscador de cursos que funciona directamente en la pagina
- y este Readme
- en la parte de cursos puse los 2 formularios
- cree el usuario profesor clave Final2323
- Le di un par de toques de front a la web aunque desconozco totalmente HTML, fui siguiendo lo que fue haciendo el profe en las clases
 y fui adaptando segun lo que necesitaba hacer
 
- Creado el CRUD de READ para ver la lista de profesores

- Creado el CRUD de CREATE para agregar profesores

- Creado el CRUD para eliminar profesores

- Creado el CRUD para editar profesores

- Cambie la vista de la lista de profesores, se puede ver y editar de una mejor manera

- Arreglado el login y register falta logout

- Cambiada la pagina de profesores LISTA

- Hay que arreglar el formulario de registro de estudiantes y que vaya directo a estudiantes en la base de datos

- Arreglado el logout, y edicion de perfiles de usuario, aunque todavia no se pueden cambiar las contraseñas

- Arreglada la vista, ahora muestra el usuario logeado, estan los links para editar el perfil y desloguearse

- muchos cambios no recuerdo cuales, hay que borrar la BD de nuevo y subirla de nuevo, agregar en cursos el nombre de profesor y a los formularios
tambien hay que hacer que dependiendo del tipo de usuario que este logeado en la pagina que tenga distintos permisos de vista y si puede borrar o editar

HAY QUE ARREGLAR EL LOGIN QUE MUESTRE UN MENSAJE O ALGO DESPUES DE LOGEARSE Y DESPUES DE REGISTRARSE                 success_url = reverse_lazy('home')

HAY QUE RESTRINGIR EL ACCESO A DISTINTAS CUENTAS QUE NO SEAN DE STAFF/ADMIN 

Increible, ya funciona todo, hay que restringir acceso a distintas partes de la pagina para staff y regular user, despues hacer el video mostrando como funciona la pagina, COMPLETAR EL EXCEL CON LAS PRUEBAS y listo !!!! ENTREGAR !!!!