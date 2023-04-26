# Clase 05 - Building a Robust Front End in Django.

En esta clase se vieron los temas:
* **Static Files.**
* **How to set up a base HTML for every Django Template.**
* **Style.**

***
## Static files.

Es necesario crear un folder con el nombre de static, dentro de esta carpeta van a ir todos nuestros archivos estáticos asi como css, js, imágenes, videos, etc.

Una vez creado el folder es necesario agregarlo a nuestro archivo de **settings.py** casi al final debajo de **STATIC_URL**.

Ejemplo:

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/4.2/howto/static-files/

    STATIC_URL = 'static/'
    STATICFILES_DIRS = [
        BASE_DIR / 'static'
    ]

Para esta clase se va a crear un archivo css que le dará estilo a nuestro html NotesView.

Dentro del folder **"static"** se creara el siguiente archivo. **_static/css/style.css_** y se agregara lo siguiente.

    .note-li{
        color: red;
    }

Una vez echo esto, tenemos que mandar a llamar nuestro archivo de estilo dentro de nuestro html