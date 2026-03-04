import math
def promedio(vector):
    suma=0
    for k in range(len(vector)):
        suma+= vector[k] 
    return suma/ len(vector)
def desviacion(vector):
    suma=0
    for i in range(len(vector)):
        suma+= (vector[i] - promedio(vec))**2  
    return math.sqrt(suma/(n-1))
vec = []
n = int(input("ingrese el numero de datos: "))
for i in range(n):
    x=float(input("ingrese los datos: "))
    vec.append(x)
print(f"el promedio es: {promedio(vec)} ")
print(f"la desviación estándar es: {desviacion(vec)} ")
