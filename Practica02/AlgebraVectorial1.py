import math

class AlgebraVectorial:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y  
        self.__z = z  

    def __add__(self, other):
        return AlgebraVectorial(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return AlgebraVectorial(self.__x * other, self.__y * other, self.__z * other)
        else:
            return (self.__x * other.__x + self.__y * other.__y + self.__z * other.__z)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __pos__(self):
        return math.sqrt(self.__x**2 + self.__y**2 + self.__z**2) 

    def __neg__(self):
        return AlgebraVectorial(-self.__x, -self.__y, -self.__z)

    def __sub__(self, other):
        return AlgebraVectorial(self.__x - other.__x, self.__y - other.__y, self.__z - other.__z)

    def __pow__(self, other):
        return AlgebraVectorial(
            self.__y * other.__z - self.__z * other.__y,
            self.__z * other.__x - self.__x * other.__z,
            self.__x * other.__y - self.__y * other.__x
        )    

    def __str__(self):
        return f"x: {self.__x}, y: {self.__y}, z: {self.__z}"

    def ortogonal(self, other):
        if +(self * other) == 0:
            return "son ortogonales"
        else:
            return "no son ortogonales"

    def proyeccion(self, other):
        return other * ((self * other) / (+other)**2) 


class Main:
    a = AlgebraVectorial(1,2,3)
    b = AlgebraVectorial(4,5,6)

    print("suma: ", a + b) 
    print("resta: ", a - b) 
    print("escalar: ", a * 3) 
    print("escalar: ", 2 * b) 
    print("producto punto: ", a * b) 
    print("longitud: ", +a) 
    print("norma: ", -a) 
    print("producto cruz: ", a ** b) 
    print("ortogonalidad: ", a.ortogonal(b)) 
    print("proyección: ", a.proyeccion(b)) 