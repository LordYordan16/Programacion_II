class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    def tieneSolucion(self):
        denominador = (self.__a * self.__d) - (self.__b * self.__c)
        if denominador != 0:
            return True
        else:
            return False
    def getX(self):
        numerador = (self.__e * self.__d) - (self.__b * self.__f)
        denominador = (self.__a * self.__d) - (self.__b * self.__c)
        return numerador / denominador
    def getY(self):
        numerador = (self.__a * self.__f) - (self.__e * self.__c)
        denominador = (self.__a * self.__d) - (self.__b * self.__c)
        return numerador / denominador
class Main:
    a,b,c,d,e,f = map(int,input("ingrese a, b, c, d, e, f: ").split())
    ecuacion = EcuacionLineal(a,b,c,d,e,f)
    if ecuacion.tieneSolucion() == True:
        print(f"x = {ecuacion.getX()}, y = {ecuacion.getY()}")
    else:
        print("La ecuacion no tiene solucion")
