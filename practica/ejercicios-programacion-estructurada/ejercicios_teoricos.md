1. Aspectos conceptuales
a) ¿Qué ventajas tiene la utilización de funciones?
b) ¿Hay algún cuidado en el orden en el que se pasan los parámetros a una función?
c) ¿Cuándo uso la sentencia return?
d) ¿Qué diferencia hay entre la definición y la invocación de una función?
e) ¿Qué son los parámetros formales y para qué sirven? Ejemplifique.
f) ¿Qué son los parámetros reales y para qué sirven? Ejemplifique.
g) ¿Qué significa el cuerpo de una función? Ejemplifique.
h) ¿Existen funciones sin parámetros o argumentos?
i) ¿Puede usar una letra o un número como parámetro formal? ¿Y como parámetro real?
j) ¿Puedo tener una cantidad distinta de parámetros formales que reales en una función?
k) ¿Cómo se puede implementar un módulo con solo definiciones de funciones e importarlo desde
tu programa? ¿Cuáles son las formas de importar que ofrece Python?
l) ¿Qué diferencias hay entre los siguientes códigos?
a. import math
b. from math import sqrt


R:

a) La ventajas principales son:
    1. La reutilizacion del codigo.
    2. Permite separar los componentes del programa por partes.
    3. Ayuda a disminuir errores.
    4. Simplifica la creación, depuración y posteriores mejoras del programa.

b) Si hay un orden es el siguiente:
    a. Definir la palabra clave para la funcion
    b. identificador
    d. Parentesis
    e. Lista de parametros(Puede ser opcional)
    f. Palabra reservada para devolver un valor/resultado (Opcional)

c) El uso de la sencuencia return se usa para devolver un valor o resultado esperado de la funcion.

d) La diferencia entre un definicion y una invocacion de una funcion es que la definicion vos le decis los parametros osea las cosas que irian dentro de la funcion y la invocacion es vos estarias llamando la funcion para que ejecute con los parametros dados.

# Definición de la función con un parámetro formal 'nombre'
def saludar(nombre):
    print(f"Hola, {nombre}!")

# Llamada a la función con un argumento 'Lucía'
saludar("Lucía")

e) Los parametros formales son las parametros que le damos una funcion por ejemplo nombre, aun no tiene valor y sirve para recibir datos desde fuera de la función, hacer funciones más generales y reutilizables y trabajar con esos datos dentro del cuerpo de la función.

# Definición de la función con un parámetro formal 'nombre'
def saludar(nombre): #Aun no tiene valor.
    print(f"Hola, {nombre}!")

# Llamada a la función con un argumento 'Lucía'
saludar("Lucía")

f)  Los parametros reales son aquellos que damos a la funcion y que le damos un valor y sirve para recibir datos desde dentro de la función, hacer funciones más generales y trabajar con esos datos dentro del cuerpo de la función.

Ejemplo:

class persona():
    patas = 2 # Le estamos dando atributos en la clase

    def __init__(self, nombre): # Parametros 
        self.nombre = nombre

    def retrun_patas(self): # Metodo
        return self.patas


persona_1 = persona("Martin") # En este caso aca le estariamos pasando el parametro real

print(persona_1.retrun_patas())

g) Cuerpo de una funcion es la intruccion que esta adentro de la funcion osea es lo que hace la funcion que estamos definiendo.

h) ¿Existen funciones sin parámetros o argumentos? TODO

Si por ejemplo:

i) ¿Puede usar una letra o un número como parámetro formal? ¿Y como parámetro real? Si se puede usar una letra como parametro formal y real pero de deberse no es recomendable ya que capaz vos lo sabes pero tu compañero que lee el codigo no y un numero como parametro formal, te tiraria error y como formato real el numero pasaria sin problema.

j) ¿Puedo tener una cantidad distinta de parámetros formales que reales en una función?
De poder se puede pero a la hora de ejecutarlo te tiraria error porque cuando estaria invocando a la funcion te tiraria error que estaria faltanto los parametros formales que pusiste si le pones de mas igualmente te va a tirar porque porque no los definiste formalmente.

k) ¿Cómo se puede implementar un módulo con solo definiciones de funciones e importarlo desde
tu programa? ¿Cuáles son las formas de importar que ofrece Python?
Si se puede

Se puede crear el archivo
# mimodulo.py
def saludar(nombre):
    print(f"Hola, {nombre}")

despues podes importar toda la libreria
import mimodulo

importar una funcion especifica
from mimodolu import saludar

importar todo con * 
from mimodulo * 

y importar con alias
import mimodulo as mm

l) La diferencia fundamental radica que en el punto l.a esta importando la libreria math y en el l.b esta importando una funcion de la libreria math.