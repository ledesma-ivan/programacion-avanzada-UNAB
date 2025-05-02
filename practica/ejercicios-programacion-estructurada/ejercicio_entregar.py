''' 
¿Cuáles son los 4 pilares de la programación orientada a objetos y qué aporta cada uno?
Los 4 pilares son:

Abstraccion: Es definir los atributos y los metodos de una clase 

Encapsulamiento: Protege la inforacion de manipulaciones no autorizadas

Polimorfismo: Da la misma orden a varios objectos que respondan de diferentes maneras

Herencia: Las clases hijos heredan atributos y metodos de las clases padres

1. La diferencia principal es que en abstracion definimos los atributos y metodos de las clases en ancapsulamiento lo que hacemos es proteger las variables para que no se puedan modificar 

2. El pilar que permite sobreescribir metodos el polimorfisimo.
'''

class Dog:
 def __init__(self, name):
     self.name = name
 def speak(self):
    return "woof"
dog = Dog("Bobby")
print(dog.name)

''' 
Eercicio:
Define una jerarquía simple para vehículos con al menos una clase base y dos clases hijas.
Cada clase hija debe tener un método propio sobrescrito que imprima información
diferente. Crea una función que reciba un vehículo y llame a ese método.

Reflexión individual
¿Qué pilar sentís que dominás mejor? ¿Cuál te cuesta más aplicar en la práctica?
Abstraccion domino mejor y Encasulamiento me cuesta. 

Desafío opcional
Agregá encapsulamiento con atributos privados y métodos get y set

''' 

class Vehiculo:
    def __init__(self, ruedas, puertas):
      self.ruedas = ruedas
      self.puertas = puertas

    def set_ruedas(self, ruedas):
       self.ruedas = ruedas

    def get_info(self): 
        print(f"Tiene: {self.ruedas} y {self.puertas} puertas")

class auto(Vehiculo):
    def __init__(self, ruedas, puertas, tipo_nafta):
       super().__init__(ruedas, puertas)
       self._tipo_nafta = tipo_nafta # Aplicamos encapsulamiento.

    # Aplico polimorfismo
    def get_info(self): 
        print(f"Tiene: {self.ruedas} y {self.puertas} puertas y su tipo de nafta es: {self._tipo_nafta}")

    def set_tipo_nafta(self, tipo_nafta):
       self.tipo_nafta = tipo_nafta

class moto(Vehiculo):
    def __init__(self, ruedas, puertas, modelo):
      super().__init__(ruedas, puertas)
      self._modelo = modelo # Aplicamos encapsulamiento.

    def set_modelo(self, modelo):
       self.modelo = modelo

    # Aplico polimorfismo
    def get_info(self): 
        print(f"Tiene: {self.ruedas} y {self.puertas} puertas y su tipo de nafta es: {self._modelo}")

auto = auto(4, 4, "GNC")
auto.get_info()
auto.set_ruedas(2)
auto.get_info()

moto1 = moto(2, 0, "Yamaha MT-07")
moto1.get_info()  