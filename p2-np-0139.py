import numpy as np
# Alexander NC = 0139
# Ejemplos de numpy
print("--Espaciado linealmente en array -- 0139")
arre=np.linspace(start=0,stop=5,num=5)
print(arre)
print("--Espaciado identidad en array -- 0139")
matrix=np.eye(3)
print(matrix)
print("--Genere numeros al azar en 2D array -- 0139")
numale=np.random.random((3,4)) # genera 12 numeros aleatorios
print(numale)
print("genera 9 nuevos aleatorios entre 0 y 1")
numale=np.random.random((3,3)) # genera 12 numeros aleatorios
print(numale)
#Como generar numeros 9 aleatorios entre 1 y 20 con numpy en un arreglo de 3 por 3
print("genera 9 nuevos aleatorios entre 1 y 20")
arre = np.random.randint(1, 21, size=(3, 3))
print(arre)
print("Alexander Salazar NC = 0139")