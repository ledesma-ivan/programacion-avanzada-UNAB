# Ejercicio 2:

class Punto():
    def __init__(self, eje_x, eje_y):
        self.eje_x = eje_x
        self.eje_y = eje_y

    def get_eje_x(self):
        return self.eje_x

    def get_eje_y(self):
        return self.eje_y

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


class Punto:
    pass

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
        cambio_titulo = self.titulo = titulo
        return cambio_titulo

    def set_autor(self, autor):
        cambio_autor = autor
        return cambio_autor


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
