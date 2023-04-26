# Clase 08 - Style to our forms.

En esta clase se vieron los temas:
* **Forms style.**



***
## Forms style.
En la forma que se creo en la clase anterior podemos implementar diferentes estilos. De esta manera nuestras formas no seran estaticas y aburridas.

Ejemplo:

    from django import forms

    from django.core.exceptions import ValidationError

    from .models import Notes


    class NotesForm(forms.ModelForm):
        class Meta:
            model = Notes
            fields = ('title', 'text')

            widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'text': forms.Textarea(attrs={'class' : 'form-control', 'rows': '15'})
            }

            labels = {
                'text': 'Write your thoughts here:'
            }

        def clean_title(self):
            title = self.cleaned_data['title']

            if 'Django' not in title:
                raise ValidationError('We only accept notes about Django!')
            return title

De esta forma podemos tener el mismo estilo que se estaba utilizando antes de cambiar el formato de notes_form.html