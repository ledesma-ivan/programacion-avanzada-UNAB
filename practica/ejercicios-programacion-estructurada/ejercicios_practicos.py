#Ejercicio 1:
# a) Dado el siguiente código indique cuáles son los parámetros reales y los formales:
#Definición de funciones
def sumaAlcuadrado(x, y):
    rta= x**2 + 2*x*y + y**2
    return rta
#Programa principal
print ("Bienvenidos/as a la Suma al Cuadrado")
a=input("Ingrese el valor de a: ")
b=input("Ingrese el valor de b:")
print (sumaAlcuadrado(a, b))

# RTA: Los paremetros reales son: a, b los formales serian x, y, osea cuando se llama la funcion son los reales y los formales son por definicion de la funcion


# b)Mencione los errores en los siguientes códigos. Justifique:
# a) 
    def suma(par1, par2):
print(par1+par2)
suma()
# b) 
def suma(par1, par2):
print (par1 + par2)
print(suma(12, 10))
# c) 
def suma(par1, par2):
    return (par1 + par2)
suma(12, 10)

# d) 
 def suma(par1):
    return (par1 + 2)
suma(12, 10)

"""
Respuestas:
a: El codigo esta mal identado y ademas se hace un print de la suma y no hay un retorno donde se llama correctamente con las funciones adecuadas la suma
b. codigo mal identado y mismo errores que antes y ademas no se llama al return para devolver la suma 
c. El codigo es el correcto.
d. Esta casi bien pero no falta parametros b, definir un parametro mas para que se ejecute bien.
"""

"""
Ejercicio 2: Definir una función denominada imprimir_mensaje que imprima el siguiente mensaje en
pantalla: “Estudiando en la UNAB”. No recibe ninguna información por lo tanto no tiene ningún
parámetro formal.
"""

def imprimir_mensaje():
   mensaje = "Estudiando en la UNAB"
   print(mensaje)

imprimir_mensaje()

"""  
Ejercicio 3: Definir una función denominada retorno_mensaje que retorne siguiente mensaje:
“Estudiando en la UNAB”.
A. ¿Cómo hago para mostrar ese mensaje en pantalla?
B. ¿Qué diferencia encuentra con el ejercicio anterior?
C. Si tuvieras que imprimir mensajes como “Estudiando Matemática I en la UNAB“ y
“Estudiando Python en la UNAB” utilizando la misma función ¿Cómo la modificarías?
"""

def retorno_mensaje(mensaje):
   return mensaje

resultado = retorno_mensaje("Estudiando Python en la UNAB en la UNAB")
resultado1 = retorno_mensaje("Estudiando Matemática I en la UNAB")
"""
Respuestas:
a) Poniendo el return y el devuelva el argumento dado
b) La diferencia es como se presenta la funcion en el anterior ya quedaba fijo el mensaje y en este lo podes modificar
c) La forma de resolver seria cambiando o creado con el valor dado cuando llamo a la funcion
"""

"""  
Ejercicio 4: Definir una función denominada imprimo_fecha que reciba tres cadenas de caracteres
como parámetros formales, que representan un día, un mes y un año e imprima la fecha de la
siguiente manera: “ 21 de septiembre de 2025”."
"""""
""

def imprimo_fecha(dia, mes, año):
   print(f"{dia} de {mes} de {año}")

imprimo_fecha(25, "Septiembre", 2025)

"""
Ejercicio 5: Definir una función denominada cuantos_dias que reciba el número de mes como
parámetro y retorne la cantidad de días que posee. Ejemplo: cuantos_dias(1), debería retornar 31.
Ayuda: Pensar en tener una lista de la siguiente manera: [[“enero”,31], [“febrero”, 28], ...]
"""


def cuantos_dias(num_mes):
    meses = [
        ["enero", 31],
        ["febrero", 28],  # 29 en años bisiestos
        ["marzo", 31],
        ["abril", 30],
        ["mayo", 31],
        ["junio", 30],
        ["julio", 31],
        ["agosto", 31],   
        ["septiembre", 30],
        ["octubre", 31],
        ["noviembre", 30],
        ["diciembre", 31]]

    
    # Pensar en la logica, lapiz y papel
    if  1 <= num_mes <= 12:
        # Lo que hace es lo siguiente
        # Hacer a la lista meses con el indice dado en el numero del mes pero se le resta 1 para que concrete bien los index 
        # y despues se le pone [1] para que muestre el numero nomas 
        return meses[num_mes[0] - 1][0]
    else:
       # Numero no valido
       return None



# Ejercicio 6: Definir una función que reciba un número como parámetro y mostrar la tabla de
# multiplicar de dicho número.



def multiplicar(numero_de_la_tabla):
    lista = []
    for n in range(11):
        resultado = n * numero_de_la_tabla
        lista.append(resultado)
    return lista 
   
print(multiplicar(5))


def multiplicar(numero_de_la_tabla):
    for n in range(11):
        resultado = n * numero_de_la_tabla
        print(f"{numero_de_la_tabla} x {n} = {resultado}")

multiplicar(5)


""" 
Ejercicio 7: Definir una función que calcule el área de un círculo, otra que calcule el área de un
rectángulo y otra que calcule el área de un cuadrado. Analice qué parámetros deberían recibir
dichas funciones.
"""

""" 
Ejercicio 16: Definir una función llamada precio_con_iva que agrega el IVA (21%) de un producto
dado su precio de venta sin IVA."
""" 

def precio_con_iva(precio):
   precio_iva = precio + (precio * 0.21)
   return precio_iva


print(precio_con_iva(5))