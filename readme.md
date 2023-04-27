# Clase 08 - Working with existing data - CRUD - RUD.

En esta clase se vieron los temas:
* **U In the CRUD.**
* **D in the CRUD.**




***
## U in the CRUD.
Para hacer un update en nuestra aplicación existe una vista llama UpdateView, la cual puedes importar a tu archivo de vistas de la siguiente forma:

    from django.views.generic import UpdateView

Esta vista recibe como parámetros el modelo al cual se le va a estar haciendo el update, recibe una forma, y el success_url.

Ejemplo:

    class NotesUpdateView(UpdateView):
        model = Notes
        form_class = NotesForm
        success_url='/smart/notes'

De igual forma es necesario agregar su url en el archivo urls.py para que pueda ser utilizado de forma exitosa.

Ejemplo:

    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name='notes.update'),

***
## D in the CRUD.
Para eliminar algun elemento es necesario importar lo que es el DeleteView, a diferencia de otros esta clase la puedes importar de la siguiente forma:

    from django.views.generic.edit import DeleteView

Esta clase necesita como parámetros un modelo y el success_url para funcionar.

    class NotesDeleteView(DeleteView):
        model = Notes
        success_url='/smart/notes'

Esta forma a diferencia de UpdateView tendrá que tener su propio archivo html para poder hacer el borrado del elemento a utilizar.

Ejemplo:

    {% extends "base.html" %}

    {% block content %}
    <form method="POST" class="form-control">{% csrf_token %}
        <p>Are you sure you want to delete "{{notes.title}}"? </p>
        <p class="form-control alert alert-danger">This action can't be undone</p>

        <a href="{% url 'notes.list' %}" class="btn btn-secondary">cancel</a>
        <input type="submit" class="btn btn-danger" value="Confirm"/>
    </form>

    {% endblock %}

Este archivo se nombro con el nombre notes_confirm_delete.html ya que es el archivo que Django busca por defecto al utilizar esta clase. En caso de que quieras utilizar cualquier otro template puedes mandar a llamar el atributo template_name e igualarlo a la ruta donde se encuentra el template a utilizar.
