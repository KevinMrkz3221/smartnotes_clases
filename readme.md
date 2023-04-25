# Clase 03 - How Django Interacts with Databases

En esta clase se vieron los temas:
* **Introduction to ORMs.**

***

## Introduction to ORMs.

ORM es un marco/modelo de trabajo en el cual se crea una clase por cada tabla, esta clase la conocemos como el modelo, después se crea la migración.

Por ejemplo, se crea nuestra clase, después se transforma utilizando migrations en una tabla dentro de la base de datos. Cada clase Conocida como Modelo, es una tabla dentro de nuestra base de datos y cada atributo de nuestra clase es una columna.

La tabla se crea con la migración del modelo (makemigrations).

![Flujo de orm](/images/orm.png)
