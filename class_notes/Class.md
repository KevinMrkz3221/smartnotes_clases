# Class_1

## How to create a project

    django-admin startproject <project_name> .



## How run the server

    python manage.py runserver


## How to create an application

    django-admin startapp <app_name>


## Add the application 

Once we created the app we need add it to the setting.py on the variable INSTALLED_APPS

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

Once we created the view just to vizualice something we use a django.http HttpResponse yo show a clasic messages
'Hello, World!'

for this clase we will add the view on the urls.py



## TEMPLATES

Como buenas practicas es recomendado crear dentro de tu aplicacion la carpeta templates y dentro de esta carpeta otro directorio llamado igual que tu aplicacion

Por ejemplo:

    templates/home

Para esta clase se utilizo el archivo llamado welcome.html y se agrego dentro del archivo views.py


## Modularizacion

Se creara un archivo urls.py por cada aplicacion que se cree de esta manera se manejan las rutas de manera mas sensilla

dentro de nuestro main app en este caso smartnotes se inclura la libreria include y se mandara llamar de como string

Ejemplo:

    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('home.urls'))
    ]
