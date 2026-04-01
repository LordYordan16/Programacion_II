from multimethod import multimethod
import math

class AlgebraVectorial:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def productoPunto(self, otroV):
        return self.x * otroV.x + self.y * otroV.y + self.z * otroV.z

    def productoCruz(self, otroV):
        return AlgebraVectorial( self.y * otroV.z - self.z * otroV.y, self.z * otroV.x - self.x * otroV.z, self.x * otroV.y - self.y * otroV.x)

    @multimethod
    def perpendicular(self, otroV):
        return "son perpendiculares" if self.productoPunto(otroV) == 0 else "no son perpendiculares"

    @multimethod
    def perpendicular(self, otroV, x: float):

        suma = self + otroV
        return "son perpendiculares" if abs(suma.norma()**2 - (self.norma()**2 + otroV.norma()**2)) < 1e-6 else "no son perpendiculares"

    @multimethod
    def paralelo(self, otroV):
        cruz = self.productoCruz(otroV)
        return "son paralelos" if cruz.x == 0 and cruz.y == 0 and cruz.z == 0 else "no son paralelos"

    @multimethod
    def paralelo(self, otroV, x: str):
        return self.paralelo(otroV)

    def proyeccion(self, otroV):
        esc = self.productoPunto(otroV) / (otroV.norma()**2)
        return AlgebraVectorial(esc * otroV.x, esc * otroV.y, esc * otroV.z
        )

    def componente(self, otroV):
        return self.productoPunto(otroV) / otroV.norma()

    def __add__(self, otroV):
        return AlgebraVectorial(
            self.x + otroV.x, self.y + otroV.y, self.z + otroV.z
        )

    def __sub__(self, otroV):
        return AlgebraVectorial(
            self.x - otroV.x, self.y - otroV.y, self.z - otroV.z
        )

    def __mul__(self, escalar):
        return AlgebraVectorial(
            self.x * escalar, self.y * escalar, self.z * escalar
        )

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


class Main:
    a = AlgebraVectorial()
    b = AlgebraVectorial(2, 4, 6)
    c = AlgebraVectorial(1, 2, 3)

    print("a:", a)
    print("b:", b)
    print("c:", c)

    print("Perpendicular:", a.perpendicular(b))
    print("Perpendicular float:", a.perpendicular(b, 1.0))

    print("Paralelo:", b.paralelo(c))
    print("Paralelo str:", b.paralelo(c, ""))

    print("Proyección de b sobre c:", b.proyeccion(c))
    print("Componente de b en c:", b.componente(c))

    print("Suma:", b + c)
    print("Resta:", b - c)
    print("Escalar:", b * 2)