import time
import random
class Cronometro:
    def __init__(self):
        self.__inicia = int(time.time()*1000)
        self.__finaliza = None
    def getInicia(self):
        return self.__inicia
    def getFinaliza(self):
        return self.__finaliza
    def inicia(self):
        self.__inicia = int(time.time()*1000)
        self.__finaliza = None
    def detener(self):
        self.__finaliza = int(time.time()*1000)
    def lapsodetiempo(self):
        if self.__finaliza is None:
            return None
        return self.__finaliza - self.__inicia

class Main:
    vec = []
    for i in range(100000):
        vec.append(random.randint(1,100000))
    def ordenacionseleccion(lista):
        n = len(lista)
        for i in range(n):
            indmin = i
            for j in range(i+1, n):
                if lista[j] < lista[indmin]:
                    indmin = j
            lista[i], lista[indmin] = lista[indmin], lista[i]
        return lista
    c1 = Cronometro()
    c1.inicia()
    vec1 = ordenacionseleccion(vec)
    c1.detener()
    print(f"{c1.lapsodetiempo()} ms")
