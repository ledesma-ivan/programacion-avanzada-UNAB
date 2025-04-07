class Figura:
    pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado 

    def perimetro(self):
        return self.lado * 4

class Rectangulo(Figura):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1 
        self.lado2 = lado2 

    def perimetro(self):
        return 2*self.lado1 + 2*self.lado2

# TODO: Pensar en otra posible herencia (taxonomía)
# Otra forma posible seria

class Figura:
    pass

class Poligono(Figura):
    def __init__(self, lados):
        self.lados = lados

    def perimetro(self):
        return sum(self.lados)

class Cuadrado(Poligono):
    def __init__(self, lado):
        super().__init__([lado]*4)

class Rectangulo(Poligono):
    def __init__(self, lado1, lado2):
        super().__init__([lado1, lado2, lado1, lado2])

cuad = Cuadrado(5)
print("Perímetro del cuadrado:", cuad.perimetro())  # 20

rect = Rectangulo(4, 6)
print("Perímetro del rectángulo:", rect.perimetro())  # 20

# Pruebas
c1 = Cuadrado(6)
c2 = Cuadrado(4)
print(c1.perimetro())
print(c2.perimetro())

r1 = Rectangulo(3,4)
r2 = Rectangulo(4,10)
print(r1.perimetro())
print(r2.perimetro())