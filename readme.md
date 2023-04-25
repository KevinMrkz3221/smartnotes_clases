# Clase 03 - How Django Interacts with Databases

En esta clase se vieron los temas:
* **Introduction to ORMs.**
* **Creating your first model.**
* **Using admin for data creation and manipulation.**
* **Django Shell for creating and querying data.**

***

## Introduction to ORMs.

### **Object-Relational Mapping.**

ORM es un marco/modelo de trabajo en el cual se crea una clase por cada tabla, esta clase la conocemos como el modelo, después se crea la migración.

Por ejemplo, se crea nuestra clase, después se transforma utilizando migrations en una tabla dentro de la base de datos. Cada clase Conocida como Modelo, es una tabla dentro de nuestra base de datos y cada atributo de nuestra clase es una columna.

La tabla se crea con la migración del modelo (makemigrations).

### Flujo de ORM

![Flujo de orm](/images/orm.png)

***

## Creating your first model.
Para crear nuestra tabla dentro de la base de datos es necesario primero crear un modelo.

En esta clase se creara una nueva app, llamada notes. Una vez creada se van a ir a el archivo models.py y se creara la siguiente clase:

    from django.db import models

    # Create your models here.

    class Notes(models.Model):
        title = models.CharField(max_length=200)
        text = models.TextField()
        created = models.DateTimeField(auto_now_add=True)
    

Una vez creado el modelo es necesario hacer las migraciones correspondientes a este modelo, con el comando:

    python manage.py makemigration

Lo que hace make migrations es crear una plantilla de lo que sera nuestra tabla dentro de la base de datos, una vez se utiliza este comando se creara un archivo en la carpeta migrations llamado 0001_initial.py. Este archivo tiene las instrucciones con las cuales se creara la tabla dentro de la base de datos.

Para crear la tabla dentro de la base de datos se utilizara el comando:

    python manage.py migrate

Una vez utilicemos este comando se creara la tabla, pero Oh no, no se podrá visualizar dentro del Django-admin.

***
## Using admin for data creation and manipulation.

Si eres curioso e intentaste ver si se visualizaba la tabla dentro de Django-admin, te habrás dado cuenta que esta no se puede ver.

Esto es debido a que tienes que ser explicito con Django y decirle que quieres visualizar dicha tabla en el Django-admin.

Para agregar la vista de la tabla es necesario utilizar las siguientes lineas de comando dentro de la aplicación a trabajar:

    from django.contrib import admin

    from . import models
    # Register your models here.

    class NotesAdmin(admin.ModelAdmin):
        # Se muestran los datos que queremos ver en la tabla.
        list_display = ('title', 'created')

    # Decimos que vamos a utilizar el modelo Notes en la tabla de NotesAdmin.
    admin.site.register(models.Notes, NotesAdmin)

***
## Django Shell for creating and querying data.

Con Django Shell podemos consultar nuestra base de datos utilizando el comando:

    python manage.py shell

De esta forma accedemos al shell y aquí podemos hacer nuestras consultas. Las cuales serán de gran ayuda mas adelante en el proyecto.

**A continuación el Hello, World! de Django Shell:**

Este extracto lo que hace es buscar el objeto que tenga el pk (Private Key) con el valor de '1'.


    from notes.models import Notes

    mynote = Notes.objects.get(pk='1')
    mynote.title
    mynote.text

Este extracto lo que hace es obtener todos los valores de la tabla de notes

    from notes.models import Notes
    notes = Notes.objects.all()

Se pueden crear nuevas notas utilizando el comando:

    new_note = Notes.objects.create(title='A second note',  text= 'This is a second note')


Se puede filtrar utilizando los comandos:

    Notes.objects.filter(title__startswith="My")
    Notes.objects.filter(text__icontains='Django')
    Notes.objects.exclude(text__icontains='Django')

Multiples filtros:

    Notes.objects.filter(text__icontains='Django').exclude(title__icontains='Django')