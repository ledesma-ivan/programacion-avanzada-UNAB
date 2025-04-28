# Decoradores

new_class = type('myClass',(object, ),{'a' : True})

a = new_class()
a.a

# Ejemplo de creacion de una funcion decoradora sin argumentos

def my_primer_decorador(function):

    def funcion_de_retorno():
        print('Inicio ....')
        function()
        print('Fin')

    return funcion_de_retorno


@my_primer_decorador
def funcion_de_entrada():
    print('Hola mundo')


@my_primer_decorador
def input_fucion():
    print('Hola world')

if __name__ =="__main__":
    funcion_de_entrada()
    print()
    input_fucion()



'''
Ejercicio 1:
a) Rehaga al menos 3 clases con el constructor type
b) ¿Cómo se deben definir los métodos con el constructor type?
'''



''' 
Ejercicio 2:
a) Defina una función de nombre mensaje, la cual debe imprimir “Esto es Programación Avanzada”, la cual a través de un decorator poder
imprimir el texto “Hola” y “Chau”, La salida debe ser de la forma:
Hola
Esto es Programación Avanzada.
Chau
a) Programar un decorador que en caso de querer dividir por 0 emita un mensaje por pantalla. Integrar en un ejemplo
b) Programar un decorador para que imprima la fecha y hora. Integrar en un ejemplo.
c) Investigar: i) Cómo invocar a 2 decoradores a la vez?
 ii) Cómo invocar a un decorador que está programado en otro archivo?
'''