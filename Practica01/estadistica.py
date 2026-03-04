import math
class Estadistica:
    def __init__(self, vector, n):
        self.__vector = vector
        self.__n = n
    def promedio(self):
        suma=0
        for i in range(len(self.__vector)):
            suma+= self.__vector[i] 
        return suma/self.__n
    def desviacion(self): 
        suma=0
        for i in range(len(self.__vector)):
            suma+= (self.__vector[i] - self.promedio())**2  
        return math.sqrt(suma/(self.__n -1))
class Main:
    vec = []
    n = int(input("ingrese el numero de datos: "))
    for i in range(n):
        x=float(input("ingrese los datos: "))
        vec.append(x)
    estadistica1 = Estadistica(vec, n)
    print(f"el promedio es: {estadistica1.promedio()}")
    print(f"la desviación estándar es: {estadistica1.desviacion()}")
