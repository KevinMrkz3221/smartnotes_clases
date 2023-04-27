# Clase 12 - Using Django to Store and Display User-Specific Data

En esta clase se vieron los temas:

* **ForeignKey: How Models relate to each other.**
* **Displaying only the logged user data.**
* **Adding a new note after ForeignKey.**

***
## **ForeignKey: How Models relate to each other.**

Cuando creas tu propio modelo existe la posibilidad de hacer relaciones entre tablas mediante un ForeignKey. Esto tiene que ver mas con el diseño de la base de datos, es recomendado generar bases de datos que se encuentren plenamente normalizadas para que de esta forma nuestra aplicación web funcione de manera rápida.

Para agregar un ForeignKey a nuestro modelo unicamente es necesario añadir las siguientes lineas de código:

    from django.contrib.auth.models import User

Y dentro de nuestro modelo

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

De esta forma le estamos diciendo que se va a traer específicamente las notas del usuario en uso.

Una vez hechos estos cambios en nuestro modelo, es necesario generar las migraciones con el comando:

    python manage.py makemigrations

Para después utilizar:

    python manage.py migrate.

Al realizar estos campos Django se dará cuenta que muy probablemente tienes elementos en este caso notas creadas y que sera necesario proporcionar un id de algún usuario para agregarlo por defecto en todos los registros para que asi la migración se haga de manera efectiva. También te dará la opción de agregar una a una el id a cada nota, por esta cuestión se recomienda utilizar la primera opción.

**Nota:**
Si al momento de hacer la migración proporcionas un id que no existe, la migración no sera exitosa, asegúrate de generar la migración con un id existente para que no tengas ningún inconveniente.

***
## **Displaying only the logged user data.**
Para mostrar unicamente la información del usuario en cuestión tenemos que devolvernos a la Clase_06, donde se explico como implementar LoginRequiredMixin.

Una vez aplicado este paso a todas nuestras vistas, se necesitara modificar uno de los métodos que heredamos de la clase ListView, mas en especifico, el método **get_queryset**.

Este método se encarga de hacer el query que nos muestra toda la lista de los elementos que tenemos dentro de nuestra base de datos, el problema es que no hace la distincion entre usuarios.

Unicamente se necesita agregar la siguiente linea de código en la vista.

    def get_queryset(self):
        return self.request.user.notes.all()

Una vez hecho estos pasos nuestra vista tiene que quedar de la siguiente manera.

    class NotesView(LoginRequiredMixin, ListView):
        model = Notes
        context_object_name = "notes"
        template_name = "notes/notes_list.html"
        login_url = '/admin'

        def get_queryset(self):
            return self.request.user.notes.all()

Una vez realizados los pasos se podrán visualizar las notas de el usuario en cuestión.

***
## **Adding a new note after ForeignKey.**

Al cambiar la estructura de nuestra tabla, sera necesario agregar un usuario al objeto que estaremos intentando crear, dado que si intentamos crear una nueva nota sin pasarle el parámetro de user id, esto nos arrojara un error que no nos permitirá crear la nota.

Al igual que en el tema anterior sera necesario modificar una de las funciones de nuestra clase NotesCreateView, mas en especifico el método **form_valid** y se hace de la siguente forma.

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

Esto lo que ara es pasar el id o ForeignKey del usuario en cuestión, asi completando lo que es el formulario entero para que se pueda guardar en nuestra tabla.
