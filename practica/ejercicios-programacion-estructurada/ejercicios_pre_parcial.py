'''
1. Programacion imperativa:

. ¿Verdadero o falso? La programación imperativa se basa en describir qué se quiere
lograr, no cómo.

Falso al termino que te estas referiendo es la programacion descriptiva en este caso se basa como se quiere lograr, el paso a paso resolver el problema.


2. ¿Qué estructuras básicas componen la programación imperativa?
Los bucles for, while y las condicionales and, or, if, else, elif, que permite que se ejecute las decisiones.

'''


nums = [1, 2, 3, 4]
lista_new = []

for i in nums:
    if i % 2 == 0:
        x = i * 2
        lista_new.append(x)
print(lista_new)

# Corregir para que solo los pares se dupliquen y la salida sea una nueva
# lista.

'''
Ejercicio práctico:
Crea una función que reciba una lista de números y devuelva otra lista con solo los números
pares multiplicados por 3, usando solo estructuras imperativas (no comprensiones ni
funciones como map o filter)
'''

lista = [2, 3, 4, 5]

lista_nueva = []
for i in lista:
    if i % 2 == 0:
        x = i * 3
        lista_nueva.append(x)
print(lista_nueva)


'''
¿Qué diferencias notaste entre escribir código imperativo y usar comprensiones o funciones
como map o filter?

En que en la las compresiones pueden ser mas confunsa si no entendes mucho de listas, pero es mas funcional

� Desafío opcional
Convertí el mismo ejercicio imperativo a uno declarativo (usando list comprehension) y
compará claridad y legibilidad.
'''
nums = [1, 2, 3, 4]
lista_new = []

# Usando map y filter repasar un poco aca.

# filter: se usa para filtrar elementos segun condicion
# map se usa una funcion a cada elemento de la lista

# lambda argumentos: expresión , condicion, elemento
lista_filtrada = filter(lambda x: x % 2 == 0, lista)

# Map
lista_nueva_map = list(map(lambda x: x * 2, lista_filtrada))
print(lista_nueva_map)


# [expresión for elemento in iterable if condición]

pares = [i * 2 for i in nums if i % 2 == 0]
print(pares)
