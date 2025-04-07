"""En base a un ejemplo que plantee el uso de dos clases con la relación “es un” definir:
● Nombre de cada clase
● Propiedades (al menos 2 por cada clase) Hecho
● Métodos (al menos 2 por cada clase) Hecho
● Instanciación de Objetos (al menos 2 objetos por cada clase) Hecho
Cómo estima que cumple con los pilares de la POO.
● Encapsulamiento Es proteger los datos internos y que no se puedan acceder desde fuera. Hecho con ._ o si se quiere mas privado es .__ Hecho
● Abstracción Es octular detalles innecesarios  y mostrar lo importante.  Hecho
● Herencia Aplicado herencia de la clase usuario padre a la clase publicacion hija Hecho
● Polimorfismo Es invocar a la variable y que actue de diferente forma cuando se lo invoca en otra clase Hecho
"""

class Usuario():
    def __init__(self, nombre, email, contraseña):
        self.nombre = nombre
        self.email = email
        self.__contraseña = contraseña # Encapulado (protegido)
        
    def verificar_nombre(self, nombre):
        return self.nombre == nombre

    def verificar_contraseña(self, contraseña):
        return self.__contraseña == contraseña
    
    def mostrar_info(self):
        return f" {self.nombre} y su correo: {self.email}"

# Herencia
class Publicacion(Usuario):
    def __init__(self, nombre_de_publicacion, nombre, email, contraseña): # Importante traer los parametros del otro aunque algunos no los usemos 
        super().__init__(nombre, email, contraseña) 
        self.nombre_de_publicacion = nombre_de_publicacion

    def mostrar_info(self): # Mismo metodo pero diferente compartamiento
        return f" {self.nombre} del autor y correo: {self.email} y el nombre de la publicacion es {self.nombre_de_publicacion}"
    
    def cambiar_nombre_publicacion(self, nombre_de_publicacion): 
        self.nombre_de_publicacion = nombre_de_publicacion

# Creamos las instancias
user = Usuario("Pedro", "Martin@gmail.com", "456testing")
user2 = Usuario("Juan", "Perez@gmail.com", "testing456")

# Instancias de publicacion
public = Publicacion("1 y 1000 noches", "Pedro", "Martin@gmail.com", "456testing")
public_2 = Publicacion("Mi primera chamba", "Juan", "Perez@gmail.com", "testing456")

# Imprimimos las instancias con un metodo aplicado
print(user.mostrar_info()) # Mostramo la informacion del nombre y su correo
print(user.verificar_nombre('Martin'))
print(user.verificar_contraseña('456testing'))
print(user2.mostrar_info())


# Imprmimos resultados de publicacion
print(public.mostrar_info())
print(public_2.mostrar_info())

# Cambiamos el nombre del titulo
public_2.cambiar_nombre_publicacion("El titulo cambiante") 
print(public_2.mostrar_info())
