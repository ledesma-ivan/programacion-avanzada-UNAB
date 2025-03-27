""" Ejercicio 0.0 (La de la encuesta):
 Programar preferentemente en Python la siguiente consigna utilizando funciones y parámetros:
 Calcular el área y el perímetro de un cuadrado, de un rectángulo y de una circunferencia.
 Realizar las invocaciones a las distintas funciones definidas anteriormente.

 Nota 1: No utilizar por favor ninguna IA generativa (ChatGPT, DeepSeek, entre otras), sino realizarlo desde el conocimiento propio o "googleando" solamente.
 Nota 2: Como recomendación puede realizar este challenge (desafío) usando el paradigma de programación estructurado o el orientado a objetos (opcional).
"""


def cuadrado(lado):
    area = lado * lado
    perimetro = 4 * lado
    mensaje = "El Area es: {area}, y su perimetro es {perimetro} del cuadrado"
    return mensaje


def rectangulo(ancho, alto):
    area = ancho * alto
    perimetro = (2 * ancho) / (2 * ancho)
    mensaje = "El Area es: {area}, y su perimetro es {perimetro} del rectangulo"
    return mensaje


def circunferencia(radio):
    area = 3.14 * radio ** 2
    perimetro = 2 * 3.14 * radio
    mensaje = "El Area es: {area}, y su perimetro es {perimetro} circunferencia"
    return mensaje


print(cuadrado(2))
print(rectangulo(2, 4))
print(circunferencia(2))

# Alternativa opcional:


# Ejercicio 1:
# a) Dado el siguiente código indique cuáles son los parámetros reales y los formales:
# Definición de funciones
def sumaAlcuadrado(x, y):
    rta = x**2 + 2 * x * y + y**2
    return rta


# Programa principal
print("Bienvenidos/as a la Suma al Cuadrado")
a = input("Ingrese el valor de a: ")
b = input("Ingrese el valor de b:")
print(sumaAlcuadrado(a, b))

# RTA: Los paremetros reales son: a, b los formales serian x, y, osea
# cuando se llama la funcion son los reales y los formales son por
# definicion de la funcion


# b)Mencione los errores en los siguientes códigos. Justifique:
# a)
def suma(par1, par2):


print(par1 + par2)
suma()
# b)
def suma(par1, par2):


print(par1 + par2)
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
    if 1 <= num_mes <= 12:
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


def circulo(radio):
    area = 3.14 * radio ** 2
    mensaje = "El Area del circulo es: {area}"
    return mensaje


def cuadrado(lado):
    area = lado * lado
    perimetro = 4 * lado
    mensaje = "El Area es: {area}, y su perimetro es {perimetro} del cuadrado"
    return mensaje


def circulo(ancho, alto):
    area = ancho * alto
    perimetro = (2 * ancho) / (2 * ancho)
    mensaje = "El Area es: {area}, y su perimetro es {perimetro} del rectangulo"
    return mensaje


print(circunferencia(2))
print(cuadrado(2))
print(rectangulo(2, 4))


# Prestar atencion hay veces que no se piden un parametro en la funcion.
"""
Ejercicio 8: Definir una función llamada calculo_rebaja que reciba dos números, uno con el precio
anterior y otro para el precio rebajado y devuelva un número que represente el porcentaje
rebajado.

"""


def calculo_rebaja(precio_anterior, precio_rebajado):
    # Calculamos la diferencia del precio original con el rebajado
    rebaja = precio_anterior - precio_rebajado
    # Dividimos el precio anterior con el resultado de la rebaja
    rebajando = rebaja / precio_anterior
    # Multiplimos para obtener el porcentaje final.
    resultado = rebajando * 100
    return resultado


print(calculo_rebaja(1200, 800))

# Otra forma de hacer sin argumentos o parametros


def calculo_rebaja():
    precio_anterior = float(input("Ingrese el precio anterior: "))
    precio_rebajado = float(input("Ingrese el precio rebajado: "))
    # Calculamos la diferencia del precio original con el rebajado
    rebaja = precio_anterior - precio_rebajado
    # Dividimos el precio anterior con el resultado de la rebaja
    rebajando = rebaja / precio_anterior
    # Multiplimos para obtener el porcentaje final.
    resultado = rebajando * 100
    return resultado


print(calculo_rebaja)


"""
Ejercicio 9: Definir una función llamada calculo_nuevo_precio que reciba dos números, uno con el
precio anterior y otro con el número de porcentaje a aumentar y devuelva el precio aumentado.
"""

# Forma correcta


def calculo_nuevo_precio():
    precio_anterior = float(input("Ingrese el precio anterior: "))
    porcentaje_aumentar = float(input("Ingrese el precio rebajado: "))
    precio_aumetado = precio_anterior + (precio_anterior * porcentaje_aumentar)
    return precio_aumetado


print(calculo_nuevo_precio())

# Nunca se pidio que entre como parametros


def calculo_nuevo_precio(precio_anterior, porcentaje_aumentar):
    precio_aumetado = precio_anterior + (precio_anterior * porcentaje_aumentar)
    return precio_aumetado


print(calculo_nuevo_precio(1, 0.2))


"""
Ejercicio 10: Definir una función llamada calculo_transporte que reciba cuatro números: la cantidad
de alumnos de 1era, 2da y 3er. salita de un jardín de infantes y la cantidad de asientos del
transporte escolar. La función debe retornar cuántos micros necesito contratar para una excursión
sabiendo que cada salita es acompañada por tres adultos.
"""
# Como en este caso no especifica el uso de parametro, aunque es lo ideal
# pero bueno.


def calculo_transporte():
    cantidad_alumnos_1ra = int(
        input("Ingrese la cantidad de alumnos de primer year"))

    cantidad_alumnos_2ra = int(
        input("Ingrese la cantidad de  alumnos de segundo year"))

    cantidad_alumnos_3ra = int(
        input("Ingrese la cantidad de alumnos de tercero year"))

    cantidad_sala_jardin = int(
        input("Ingrese la cantidad de infantes de la sala de jardin"))

    cantidad_asientos_trasnporte = int(
        input("Ingrese la cantidad de asientos de la sala de jardin"))

    suma_adultos = 12

    suma_total = cantidad_alumnos_1ra + cantidad_alumnos_2ra + \
        cantidad_alumnos_3ra + cantidad_sala_jardin + suma_adultos
    calculo_micros = suma_total // cantidad_asientos_trasnporte

    return f"La cantidad de micro que se necesitan es: {calculo_micros}"


# La otra forma es:
def calculo_transporte(alumnos_1era, alumnos_2da,
                       alumnos_3era, asientos_micro):
    # Calcula el total de alumnos
    total_alumnos = alumnos_1era + alumnos_2da + alumnos_3era

    # Calcula el total de adultos (4 por cada salita)
    total_adultos = 12  # 3 adultos por cada salita

    # Calcula el total de personas
    total_personas = total_alumnos + total_adultos

    # Calcula los micros necesarios
    micros_necesarios = (total_personas + asientos_micro - 1) // asientos_micro

    return micros_necesarios


"""
Ejercicio 11: Definir una función llamada armo_cartel que reciba una cadena de caracteres (para el
nombre del producto) y dos números (el precio anterior y el otro para el precio rebajado) e imprima
un cartel de la siguiente forma:
*************************************
Atención!!! Gran rebaja para el producto nombre (recibido como parámetro)
Antes: precio anterior (dato recibido como parámetro)
Ahora: precio rebajado (dato recibido como parámetro)
"""


def armo_cartel(producto_nombre, precio_anterior, precio_rebajado):
    # Calculamos la diferencia del precio original con el rebajado
    rebaja = precio_anterior - precio_rebajado
    # Dividimos el precio anterior con el resultado de la rebaja
    rebajando = rebaja / precio_anterior
    # Multiplimos para obtener el porcentaje final.
    resultado = rebajando * 100
    mensaje = f""""" *************************************
   Atención!!! Gran rebaja para el producto {producto_nombre}
   Antes: {precio_anterior}
   Ahora: {precio_rebajado} """
    return mensaje


print(armo_cartel("Test", 1, 0.2))


"""
Ejercicio 13: Definir una función llamada a_pagar que reciba 4 números: la cantidad de personas, el
monto gastado en bebida, el monto gastado en comida y el del alquiler del lugar, y retorne cuánto le
toca pagar a cada uno.
"""


def llamada_a_pagar(cantidad_pagar_personas, monto_bebida,
                    monto_comida, alquiler_del_lugar):

    resultado = (monto_bebida + monto_comida,
                 alquiler_del_lugar) / cantidad_pagar_personas
    mensaje = f"Le toca pagar a cada uno {resultado}"
    return mensaje


"""
Ejercicio 14: Definir tres funciones llamadas convertir_a_dolar, convertir_a_euro y convertir_a_real.
Cada función recibe un parámetro que representa un monto en pesos y devuelve su conversión
respectiva.
"""


def convertir_a_dolar(pesos, dolar):

    conversion_dolar = pesos / dolar

    return conversion_dolar


def convertir_a_euros(pesos, euros):

    conversion_euros = pesos / euros

    return conversion_euros


def convertir_a_real(pesos, reales):

    conversion_reales = pesos / reales

    return reales


print(convertir_a_dolar(10000, 1050))
print(convertir_a_euros(10000, 1150))
print(convertir_a_real(10000, 185))


"""
Ejercicio 15: Definir una función llamada calculo_dosis que reciba tres números. Uno para la
cantidad de días que debe suministrar el remedio, el segundo dato para la cantidad de veces por
día que debe tomarlo, y el último dato para la cantidad de comprimidos que trae el envase. La
función debe devolver verdadero si el envase alcanza para ese tratamiento y falso si no alcanza.
"""


def calculo_dosis(cantidad_dias, cantidad_de_veces_dias,
                  cantidad_de_comprimidos):

    consumo_necesario = cantidad_dias * cantidad_de_veces_dias

    if consumo_necesario >= cantidad_de_comprimidos:
        return True
    elif consumo_necesario <= cantidad_de_comprimidos:
        return False


"""
Ejercicio 16: Definir una función llamada precio_con_iva que agrega el IVA (21%) de un producto
dado su precio de venta sin IVA.
 """


def precio_con_iva(precio):
    precio_iva = precio + (precio * 0.21)
    return precio_iva


print(precio_con_iva(5))

# Ejercicios complementario
"""
Ejercicio 17:
a) Definir una función que reciba como parámetro una lista de números y retorne la suma del
primer elemento con el último.


 """
# Zona de definiciones de funciones


def sumaPrimUlt(lista):
    # -1 es el ultimo elemento de la lista
    # retorna la suma entre el primer elemento de la lista con el último
    suma = lista[0] + lista[-1]
    return suma


def promedioPrimUlt(lista):
    # retorna el promedio entre el primer elemento de la lista con el último
    promedio = (lista[0] + lista[-1]) / 2
    return promedio

# Zona del programa principal
# solicitar al usuario 3 números, armar la lista e invocar las funciones
# anteriores mostrando los #resultados


lista = []

for i in range(3):
    lista_n = int(input("Ingrese un numero"))
    lista.append(lista_n)


print(sumaPrimUlt(lista))
print(promedioPrimUlt(lista))


'''
Ejercicio 18: En este código una fracción está representada por una lista de dos elementos, el
numerador y el denominador. Por ejemplo la fracción 3⁄4 sería la lista (3,4). Complete el código
según corresponda.
'''

"""
Prestar antencion en esta caso el input es lista, no hace falta crear """
# Zona de definiciones de funciones


def cargarFraccion():
    # Solicita al usuario el numerador y denominador. Arma la fracción como
    # una lista y la retorna
    a = int(input("Ingrese el numerador: "))
    b = int(input("Ingrese el denominador: "))
    lista = []
    lista.append(a)
    lista.append(b)
    return lista


def numeradorFraccion(x):
    # Retorna el numerador que se encuentra en la fracción x, representada
    # como una lista
    if len(x) == 2:
        numerador = x[0]
        return numerador
    else:
        print("Entrada no valida")
        return None


def denominadorFraccion(x):
    # Retorna el denominador que se encuentra en la fracción x, representada
    # como una lista
    if len(x) == 2:
        denominador = x[-1]
        return denominador


def sumaFracciones(x, y):
    # Retorna la suma de las fracciones, representadas como listas
    if x == 2 and y == 2:
        numeradores = x[0] + y[0]
        denominadores = x[-1] + y[-1]
        lista = []
        lista.append(numeradores)
        lista.append(denominadores)
        return lista

    else:
        print("Entrada no valida")
        return None


def restaFracciones(x, y):
    # Retorna la resta de las fracciones, representadas como listas
    if len(x) == 2 and len(y) == 2:
        numeradores = x[0] - y[0]
        denominadores = x[-1] - y[-1]
        lista = []
        lista.append(numeradores)
        lista.append(denominadores)
        return lista

    else:
        print("Entrada no valida")
        return None


def divisionFracciones(x, y):
    # Retorna la división de las fracciones, representadas como listas:
    if len(x) == 2 and len(y) == 2:
        numeradores = x[0] / y[0]
        denominadores = x[-1] / y[-1]
        lista = []
        lista.append(numeradores)
        lista.append(denominadores)
        return lista

    else:
        print("Entrada no valida")
        return None


def multiplicacionFracciones(x, y):
    # Retorna la multiplicación fracciones, representadas como listas
    if len(x) == 2 and len(y) == 2:
        numeradores = x[0] * y[0]
        denominadores = x[-1] * y[-1]
        lista = []
        lista.append(numeradores)
        lista.append(denominadores)
        return lista

    else:
        print("Entrada no valida")
        return None


# Zona del programa principal
print("Bienvenidos / as a cuentas con Fracciones")
a = cargarFraccion()
b = cargarFraccion()
print("El denominador de la primera fracción es:", numeradorFraccion(a))
print("El numerador de la segunda fracción es:", frac2.numerator)
print("La suma de dichas fracciones es:", frac1 + frac2)
print("La resta de dichas fracciones es:", frac1 - frac2)
print("La multiplicación de dichas fracciones es:", frac1 * frac2)
print("La división es:", frac1 / frac2)


'''
3. Ejercicios extras utilizando programación orientada a objetos

Ejercicio 19: Implemente el Ejercicio 14 utilizando clases. Realice las correspondientes
invocaciones a cada uno de los métodos.
Ejercicio 20: Implemente el Ejercicio 18 utilizando clases. Realice las correspondientes
invocaciones a cada uno de los métodos.
'''
