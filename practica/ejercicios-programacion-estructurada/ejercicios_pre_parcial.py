'''
1. Programacion imperativa:

. ¿Verdadero o falso? La programación imperativa se basa en describir qué se quiere
lograr, no cómo.

Falso al termino que te estas referiendo es la programacion descriptiva en este caso se basa como se quiere lograr, el paso a paso resolver el problema.


2. ¿Qué estructuras básicas componen la programación imperativa?
Los bucles for, while y las condicionales and, or, if, else, elif, que permite que se ejecute las decisiones. 

'''


nums = [1,2,3,4]
lista_new = []

for i in nums:
 if i % 2 == 0:
   x = i * 2
   lista_new.append(x)
print(lista_new)  

# Corregir para que solo los pares se dupliquen y la salida sea una nueva lista.

'''  
Ejercicio práctico:
Crea una función que reciba una lista de números y devuelva otra lista con solo los números
pares multiplicados por 3, usando solo estructuras imperativas (no comprensiones ni
funciones como map o filter)
'''