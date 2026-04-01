from multimethod import multimethod


class MiPunto:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def __str__(self):
        return f"({self.__x}, {self.__y})"
    
    @multimethod
    def distancia(self, p):
        return ((self.__x - p.getX())**2 + (self.__y - p.getY())**2)**0.5

    @multimethod
    def distancia(self, x: float, y: float):
        return ((self.__x - x)**2 + (self.__y - y)**2)**0.5
    
class Main:
    p1 = MiPunto()            
    p2 = MiPunto(10, 30.5)  
    print("Punto 1:", p1)
    print("Punto 2:", p2)
    print("Distancia:", p1.distancia(p2))