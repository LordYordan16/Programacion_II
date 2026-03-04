import math
class EcuacionesCuaraticas:
    def __init__(self, a, b, c):
        self.__a = int(a)
        self.__b = int(b)
        self.__c = int(c)
    def getDiscriminante(self):
        return ((self.__b**2) - (4 * self.__a * self.__c))
    def getRaiz1(self):
        return  (-1*self.__b + math.sqrt(self.getDiscriminante())) / 2*self.__a
    def getRaiz2(self):
        return  (-1*self.__b - math.sqrt(self.getDiscriminante())) / 2*self.__a
class Main:
    a, b, c = map(int, input("ingrese a, b, c: ").split())
    ecuacion1 = EcuacionesCuaraticas(a,b,c)
    if ecuacion1.getDiscriminante() > 0:
        print(f"la ecuacion tiene dos raices: {ecuacion1.getRaiz1()} y {ecuacion1.getRaiz2()}")
    elif ecuacion1.getDiscriminante() < 0:
        print("la ecuacion no tiene soluciones reales")
    elif ecuacion1.getDiscriminante() == 0:
        print(f"la ecuacion tiene una raiz {ecuacion1.getRaiz1()}") 
