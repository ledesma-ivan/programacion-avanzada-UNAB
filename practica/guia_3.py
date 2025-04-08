# Ejercicio 2:

class Punto():
    def __init__(self, eje_x, eje_y):
        self.eje_x = eje_x
        self.eje_y = eje_y

    def get_eje_x(self):
        return self.eje_x

    def get_eje_y(self):
        return self.eje_y

    # Es necesario para aplicarlo en el siguiente ejercicio el 3
    def set_eje_x(self, eje_x):
        self.eje_x = eje_x

    def set_eje_y(self, eje_y):
        self.eje_y = eje_y

    def impresion(self):
        print({self.eje_x}, {self.eje_y})

    def opuesto(self):
        return Punto(-self.eje_x, -self.eje_y)

    # Es necesario ya que cuando alguien haga print(objeto), mostrá esto, en
    # este caso es para el opuesto.
    def __str__(self):
        return f"({self.eje_x}, {self.eje_y})"


# Realizamos la invocaciones.
puntos = Punto(3, 4)
print(puntos.get_eje_x())
print(puntos.get_eje_y())
print(puntos.impresion())
print(puntos.opuesto())

# Ejercicio 3:


class Linea:
    def __init__(self, punto_a, punto_b):
        self.punto_a = punto_a
        self.punto_b = punto_b

    def mueve_derecha(self, d):
        self.punto_a.set_eje_x(self.punto_a.get_eje_x() + d)
        self.punto_b.set_eje_x(self.punto_b.get_eje_x() + d)

    def mueve_izquierda(self, i):
        self.punto_a.set_eje_x(self.punto_a.get_eje_x() - i)
        self.punto_b.set_eje_x(self.punto_b.get_eje_x() - i)

    def mueve_arriba(self, a):
        self.punto_a.set_eje_y(self.punto_a.get_eje_y() + a)
        self.punto_b.set_eje_y(self.punto_b.get_eje_y() + a)

    def mueve_abajo(self, ab):
        self.punto_a.set_eje_y(self.punto_a.get_eje_y() - ab)
        self.punto_b.set_eje_y(self.punto_b.get_eje_y() - ab)


# Invocaciones
punto_a = Punto(2, 4)
punto_b = Punto(3, 5)

distancia_derecha = 1 
# Guarda la instancia en la variable mi_linea
mi_linea = Linea(punto_a, punto_b)

mi_linea.mueve_derecha(distancia_derecha)
print(f"Punto A después de mover a la derecha: {mi_linea.punto_a}")
print(f"Punto B después de mover a la derecha: {mi_linea.punto_b}")

distancia_izquierda = 2
mi_linea.mueve_izquierda(distancia_izquierda)
print(f"Punto A después de mover a la izquierda: {mi_linea.punto_a}")
print(f"Punto B después de mover a la izquierda: {mi_linea.punto_b}")

distancia_arriba = 2
mi_linea.mueve_arriba(distancia_arriba)
print(f"Punto A después de mover arriba: {mi_linea.punto_a}")
print(f"Punto B después de mover arriba: {mi_linea.punto_b}")

distancia_abajo = 2
mi_linea.mueve_abajo(distancia_abajo)
print(f"Punto A después de mover arriba: {mi_linea.punto_a}")
print(f"Punto B después de mover arriba: {mi_linea.punto_b}")


# Ejercio 4:
class Cancion:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def set_titulo(self, titulo):
        self.titulo = titulo
        return self.titulo

    def set_autor(self, autor):
        self.autor = autor
        return self.autor


# Realizo las invocaciones
cancion_ej = Cancion("Dame fuego", "Sandro")
cancion_ej.get_autor()
cancion_ej.get_titulo()
cancion_ej.set_autor("Re duro, como el maestruli")
cancion_ej.set_titulo("JAJAJA")

# Ejercicio 5:
class Persona():
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

# Aplicamos herencia
class Libro(Persona):
    def __init__(self, nombre, titulo, ISBN, paginas,
                 edicion, editorial, lugar, fecha_edicion):
        super().__init__(nombre)
        self.titulo = titulo
        self.ISBN = ISBN
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.lugar = lugar
        self.fecha_edicion = fecha_edicion

    def mostrar_info(self):
        return f"""
Título: {self.titulo} {self.edicion}
Autor: {self.nombre}
ISBN: {self.ISBN}
{self.editorial}, {self.fecha_edicion}
{self.paginas} páginas
"""
persona = Persona("Liang, Y. Daniel")
libro = Libro(
    persona,
    "Introduction to Java Programming 3a. edición",
    "0-13-031997-X",
    784,
    "3a. edición",
    "Prentice-Hall",
    "New Jersey (USA)",
    "viernes 16 de noviembre de 2001")

print(libro.mostrar_info())
