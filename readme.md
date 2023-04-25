# Clase 02 - Django Built-in User Management

En esta clase se vieron los temas:

* **Crear usuarios en Django**.
> * Django Admin Interface.
> * Migrations.
> * Create Super User.
* **Django Admin**.
* **User Authentication**.



***
## Crear Usuarios.

### Django Admin interface.

Con esto podemos ver y manipular data con el gestor que tiene Django por defecto.

Para acceder a esta vista de administración es necesario ir al url:

    http://127.0.0.1:8000/admin

Pero al acceder por primera vez no tendremos accesos al administrador dado que no tenemos ningún usuario creado.

Antes de continuar al hasta este punto, el terminal nos manda un mensaje donde nos dice que no hemos migrado o que tenemos migraciones sin aplicar y nos aparece el siguiente mensaje:

    You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.


### Migrations.
La forma en que Django sabe que la información dentro de las bases de datos a sido cambiada es con los archivos llamados migrations.

Migrations explica que clase de cambios necesita para funcionar como por ejemplo **Si se creo una nueva tabla, se establecio una nueva relacion, etc.**

Para agregar estos cambios es necesario utilizar el comando **Migrate** para hacer el cambio dentro de la base de datos.

Para hacer las migraciones que el sistema necesita unicamente es necesario utilizar los comandos:

    python manage.py makemigrations
    python manage.py migrate


### Create Super User.

    python manage.py createsuperuser <name>

Para este ejemplo se utilizaran las credenciales:

    username: admin
    password: admin123

Es recomendable utilizar credenciales seguras. Django sabe de esto y si la contraseña es muy devil Django te ara la observación de que la contraseña utilizada es muy común.

**La seguridad dentro de un sistema siempre tiene que ser la prioridad numero uno**.

***

## Django Admin.

Con el administrador de Django podemos ver de manera sencilla todas las tablas que Django maneja/agrega por defecto, de igual forma, se pueden agregar nuevos usuarios o grupos de manera muy sencilla con su interfaz gráfica. Por otra parte, Django al momento de crear un nuevo usuario, este encripta la contraseña para que se almacene de manera segura dentro de nuestra base de datos.

***

## User Authentication
Para casos de autenticación en Django es muy sencillo implementarlo importando:

        from django.contrib.auth.decorators import login_required

De esta forma unicamente mandamos a llamar el decorador arriba de nuestra función/vista donde queremos pedir algún tipo de autenticación.

    @login_required

En caso de que se requiera re-diseccionar a una vista de login se puede agregar el parámetro login_url.

    @login_required(login_url='/path')