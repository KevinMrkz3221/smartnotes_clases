# Clase 04 - Building Dynamic Webpages - Part 1

En esta clase se vieron los temas:
* **Creating a dynamic template.**
* **Display content of a single note.**

***
## Creating a dynamic template.

En esta parte aprenderemos como mostrar nuestros modelos en un documento de html, para que nuestra pagina actué de manera dinámica.

Como se vio anteriormente en el render se puede enviar lo que son variables u objetos, y mostrarlos utilizando "{{<**variable**>}}" de igual forma podemos implementar lo que es un control de flujo.

Como por ejemplo, implementar la estructura FOR:

    <html>
    <title>
        Notes
    </title>

    <body>
        <h1>These are the notes</h1>

        <ul>
            {% for note in notes %}
                <li>{{note.title}}</li>
            {% endfor %}
        </ul>
    </body>

    </html>

## Display content of a single note.

En esta parte, mostraremos el detalle de una nota sola. Para esto es necesario crear su vista. Esta parte es exactamente igual a cualquier otra vista con la diferencia de que vamos a acceder al elemento por el private key del elemento

Ejemplo de función:

    def detail(request, pk):
        note = Notes.objects.get(pk=pk)

        return render(request, 'notes/note_detail.html', {'note': note})

Es necesario agregar también al archivo de urls.py de la aplicación. Ejemplo:

    urlpatterns = [
    path('notes', views.list),
    path('notes/<int:pk>', views.detail),
    ]

Donde **path('notes/<<int:pk>>', views.detail),**  int pk significa que recibirá un entero como parámetro el cual sera el private key.