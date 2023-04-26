# Clase 07 - Building a Robust Front End in Django. - Part 2

En esta clase se vieron los temas:
* **How to set up a base HTML for every Django Template.**
* **Names**


***
## How to set up a base HTML for every Django Template.

Para definir archivos base de html para todo el proyecto o mejor dicho templates, se crea una carpeta en nuestro folder static llamado **templates** y dentro del path **static/templates** van a ir todos nuestros archivos html que se utilizaran en el proyecto.

Una vez creado nuestro template es necesario agregar la ruta que se va a estar utilizando dentro del proyecto, para eso es necesario ir al **settings.py** y agregar lo siguiente en la lista de **'DIRS'**:

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                BASE_DIR / 'static/templates'
            ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

Una vez se hace esto se tiene que dar la estructura al html que se va a utilizar como base.
Ejemplo de base.html:

    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="{% static 'css/style.css' %}">
    </head>
    <body>
        {% block content %}
        {% endblock %}
    </body>
    </html>

Ahora unicamente es necesario mandar a llamar el template en los archivos html que se van a utilizar.

Ejemplo de llamada:

    {% extends "base.html" %}
    {% block content %}
        <h1>Welcome to smart Notes</h1>
        <p>Today is {{today}}</p>
    {% endblock %}



***
## Names.
Los nombres es un atributo que le podemos dar a nuestras vistas para asi mandarlas llamar mediante el html.

Por ejemplo:

    path('home', views.HomeView.as_view(), name='home'),

Podemos darle el nombre de home y al hacer click en un boton ir directo a la vista con ese nombre.

Ejemplo:

    <a href="{% url 'home' %}" class="nav-link px-2 link-secondary">Home</a>
