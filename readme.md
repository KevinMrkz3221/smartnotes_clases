# Clase 09 - Form.py.

En esta clase se vieron los temas:
* **Forms.py implementation.**
* **If Statement.**



***
## Forms.py implementation
Para hacer uso de este herramienta es necesario crear el archivo forms.py dentro de nuestra aplicacion o modulo a trabajar.

Django utiliza unas clases u objetos llamados formas. Las cuales se importan de la siguiente manera:

    from django import forms

Este es un ejemplo de la implementación de forms dentro de nuestro proyecto.

forms.py

    from django import forms
    from django.core.exceptions import ValidationError

    from .models import Notes

    class NotesForm(forms.ModelForm):
        class Meta:
            model = Notes
            fields = ('title', 'text')

        def clean_title(self):
            title = self.cleaned_data['title']

            if 'Django' not in title:
                raise ValidationError('We only accept notes about Django!')
            return title

Esta clase necesita un modelo para funcionar asi como los campos(fields) que sera necesario pedir en la forma.

Asi mismo dentro de la clase podemos agregar validaciones para asi mostrar los mensajes de manera personalizada.

Views.py

    class NotesCreateView(CreateView):
        model = Notes
        form_class = NotesForm
        success_url = '/smart/notes'

Podrás notar que el campo de fields se reemplazo por form_class haciendo referencia a la forma que se creo

***
## If Statement.
Para controlar el flujo de nuestras vistas se puede utilizar el comando if dentro de nuestro html, de esta forma podemos agregar bloques en caso de que surgir algún error o excepción.

Ejemplo:

    {% if form.errors %}
    <div class="alert alert-danger my-5">
        {{ form.errors.title.as_text }}
    </div>
    {% endif %}
