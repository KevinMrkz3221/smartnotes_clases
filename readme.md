# Clase 04 - Building Dynamic Webpages - Part 2 - Django Class-bases Views

En esta clase se vieron los temas:
* **Introduction to Django class-based views (TemplateView).**
> * **LoginRequiredMixin.**
> * **urls.py.**
> * **ListView.**


***
## Introduction to Django class-based views.

Django Class-based views son una forma de hacer el display de nuestras vistas utilizando una clase, que es a su vez una forma de modelo pero en este caso enfocado a la vista de la aplicación.
Trabajar de esta manera hace mas sencillo el darle mantenimiento a nuestras aplicaciones.

Para poder utilizar los template Views es necesario importarlos con el siguiente comando.

    from django.views.generic import TemplateView

Una vez se importa podemos crear nuestras clases que heredan de esta clase llamada **TemplateView**:

    
    class HomeView(TemplateView):
        template_name = 'home/welcome.html'
        extra_context = {'today': datetime.today()}

De esta forma queda mas elegante y es mas fácil de entender el código.
***

### LoginRequiredMixin.
Al estar trabajando con clases es recomendable utilizar **LoginRequiredMixin** para la autenticación de nuestras cuentas, esta clase da el mismo resultado de utilizar login_required. Pero cuenta con algunos módulos de seguridad que la hacen una mejor opción el implementarlo en nuestros proyectos.

Ejemplo:


    class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'


***
### urls.py
Anteriormente unicamente era necesario mandar llamar la función que hace el display de nuestra pagina. Ahora al estar trabajando con clases es necesario mandar a llamar el método de nuestra vista.

Ejemplo:

    urlpatterns = [
    path('home', views.HomeView.as_view()),
    path('authorized', views.AuthorizedView.as_view()),
    ]
***
### ListView
ListView nos ayuda a obtenerlos objetos de nuestro modelo sin la necesidad de hacer el query, la misma clase en si hace el query por nosotros.

Esta vista se importa con la siguiente linea:

    from django.views.generic import ListView

Y se utiliza de la siguiente forma:

    class NotesView(ListView):
        model = Notes
        context_object_name = "notes"
        template_name = "notes/notes_list.html"

Es necesario que la clase sepa con que modelo se va a trabajar y darle el contexto de lo que esta haciendo, que en si es generar una lista de elementos en el path /notes.

Si utilizas la convencionalismo de guardar los elementos en templates/**<app_name>** la misma clase se encarga de cargar el template si este tiene el nombre de la ruta en este caso **notes** seguida por un **"_list"** de esta forma no es necesario agregar un template_name como se hace con las funciones de las Clases anteriores.

***
### DetailView
DetailView sigue todas las reglas de ListView pero esta se encarga de obtener unicamente un elemento, se importa con la linea:

    from django.views.generic import DetailView

y se utiliza de la siguiente forma:

    class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"

En este caso la clase, maneja los errores que se vieron en la parte 1.