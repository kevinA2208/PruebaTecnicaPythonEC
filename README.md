
# Prueba Técnica Backend EnvíoClick

En este repositorio se encuentra el código de la solución a los dos ejercicios propuestos como prueba técnica backend.
## Estructura
Se encuentran 2 carpetas, *Prueba1* y *Prueba2*, en cada una se encuentra un archivo *input.py* y un archivo *main.py*.
### Input.py
En estos archivos se encuentran diferentes complementos para el código base, como por ejemplo en la prueba 1, se encuentra el párrafo de ejemplo propuesto en el Pdf de la prueba técnica, o en la prueba 2, se encuentra la lista de objetos con los registros requeridos para hacer el ordenamiento por prioridad y criterios, ademas se encuentra otra lista de objetos para introducir los criterios, de forma que en esta lista se encuentran diferentes tuplas, cada tupla es un criterio en el ordenamiento de los registros de data. La estructura de esta tupla es de ("Nombre del campo", "Operador de criterio", "Valor de criterio").
A partir de este archivo se extrae información para despues usarla en el código base, desde el archivo *main.py*
### Main.py
En este archivo se encuentra el código base con la función main, cuya función hace uso de otras funciones dependiendo de la prueba, para poder completar su solución.
También hace uso de la información guardada en su respectivo archivo *input.py*, a excepción de la palabra clave o Keyword que se requiere en la prueba 1 para poder saber cuantas veces esta la palabra en el texto o párrafo, ya que dicha palabra se solicita por medio de la consola, al hacer uso de la función *.input()*.

He utilizado algunas funciones nativas de python que he visto requeridas, como por ejemplo la función *.lower()*, ya que no veía muy necesario hacer una cadena de if para normalizar cada letra del abecedario. O por ejemplo la función .insert() en una lista, para añadir datos de otra lista al final de una en especifico.
En el código se encuentran comentarios explicativos para detallar mas el funcionamiento de cada línea o función