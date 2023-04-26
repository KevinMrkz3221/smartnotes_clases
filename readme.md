# Clase 08 - Create View.

En esta clase se vieron los temas:
* **Create, C of CRUD**



***
## Create, C of CRUD
Como cualquier sistema en veces es necesario crear formularios para crear items.


Django tiene la funcion de implementar formas segun los modelos que estamos utilizando para crear objetos y tiene una vista en especifico llamada **CreateView** la cual se importa con la siguiente linea.

    from django.views.generic import CreateView

Una vez importada la clase es necesario crear nuestra clase de vista en este caso se implementara con las notas como, NotesCreateView indicando que sera la vista de nuestro formulario.

Ejemplo:

    class NotesCreateView(CreateView):
        model = Notes
        fields = ['title', 'text']
        success_url = '/smart/notes'


Esta clase recibe como parámetros el modelo que se va a utilizar, los campos a agregar, la forma a utilizar y hacia donde queremos que se redirija la vista en caso de que se crea de manera exitosa el objeto.

