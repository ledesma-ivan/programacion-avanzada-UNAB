## Args permite poner multiples argumentos posicionales


def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print(sumar(1, 2, 3))    # Resultado: 6
print(sumar(5, 10))      # Resultado: 15

""" 
*Ejercicio 1 – Usando args
Crea una función que reciba cualquier cantidad de números y devuelva el número más grande."""

# En este caso no hace falta crear un bucle for ya que nos concentramos en los argumentos si fuera lista si.
def numeros(*args):
    maximo = max(args)
    return maximo

print(numeros(2, 3))


'''
Ejercicio 4: Promedio de números
Escribe una función que acepte una cantidad variable de números y calcule su promedio.
'''

def promedio(*args):
    promedio = sum(args) / len(args)
    return promedio

print(promedio(2,3,4))

''' 
Contar argumentos:
Crea una función que cuente cuántos argumentos ha recibido.

Mostrar los argumentos:
Crea una función que imprima uno por uno todos los argumentos que recibe.

🔁 Nivel 2: Intermedio
Filtrar solo enteros:
Crea una función que retorne una lista con solo los valores enteros de los argumentos recibidos.

Producto de los argumentos:
Crea una función que calcule el producto de todos los argumentos numéricos.

Obtener el mayor valor:
Crea una función que retorne el valor máximo entre los argumentos.

🧩 Nivel 3: Avanzado
Separar por tipo:
Crea una función que devuelva un diccionario clasificando los argumentos por tipo (int, str, etc.).

Emparejar argumentos en tuplas:
Crea una función que agrupe los argumentos en pares dentro de tuplas. Si hay un número impar de argumentos, ignora el último.

Convertir en diccionario (pares):
Crea una función que convierta los argumentos en un diccionario, usando los pares (clave, valor) recibidos.




'''
# Prestar atencion cuando se entra a args se nombra con args 
def contar_arg(*args):
    cantidad = len(args)
    return cantidad

print(contar_arg(1,2,3))


def mostrar_argumento(*args):
    for x in args:
        print(x)

mostrar_argumento(2, "el papu", 4)

'''
🔁 Nivel 2: Intermedio
Filtrar solo enteros:
Crea una función que retorne una lista con solo los valores enteros de los argumentos recibidos.

isinstance sirve para comparar objectos es una clase especifica.


Producto de los argumentos:
Crea una función que calcule el producto de todos los argumentos numéricos.
'''

def dev_entero(*args):
    for x in args:
        if isinstance(x ,int):
            print(x)

dev_entero("jose",2, "martin", 3)


# Revisar aca
def producto_arg(*args):
    for x in args:
        if isinstance(x ,int):
            total = 0
            total * x

