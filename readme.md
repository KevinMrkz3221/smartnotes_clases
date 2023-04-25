# Clase 01 - Starting you Django Project

En esta clase se vieron los temas:

* Como crear un nuevo proyecto
* Como correr el servidor
* Como crear una aplicación
* Como añadir una aplicación
* Templates
* Popularización



## How to create a project

    django-admin startproject <project_name> .



## How run the server

    python manage.py runserver


## How to create an application

    django-admin startapp <app_name>


## Add the application 

Una vez creada la aplicación es necesario añadirla dentro del archivo de settings.py en la variable de INSTALLED_APPS.

Ejemplo: 

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # APPS

        'home',
    ]

Se utilizo django.http HttpReponse para crear el clásico mensaje de **'Hello, World!'**



for this clase we will add the view on the urls.py



## TEMPLATES

Como buenas practicas es recomendado crear dentro de tu aplicación la carpeta templates y dentro de esta carpeta otro directorio llamado igual que tu aplicación

Por ejemplo:

    templates/home

Para esta clase se utilizo el archivo llamado welcome.html y se agrego dentro del archivo views.py


## Modularizacion

Se creara un archivo urls.py por cada aplicación que se cree de esta manera se manejan las rutas de manera mas sencilla

dentro de nuestro main app en este caso smartnotes se incluirá la librería include y se mandara llamar de como string

Ejemplo:

    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('home.urls'))
    ]
