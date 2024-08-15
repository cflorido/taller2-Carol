
from typing import List

#FUNCIONES
def sumarDiagonal(matriz: List[List[int]])-> int:
    suma = 0  #C1
    for i in range(len(matriz)): # C2 + C4 + C5 + n C3 
        suma += matriz[i][i] # n (2 C3 + C1)
    return suma


def revisarEntero(matriz: List[List[int]], entero: int)-> bool:
    for i in range(len(matriz)): # C2 + C5 + C6 + n C4
        for j in range(len(matriz)): # n (C2 + C5 + C6 + n C4)
            if matriz[i][j] == entero: # n^2 (2 C4 + C3)
                return True
    return False

#PARAMETROS 
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

entero = 9

#PRUEBA
print("---------Tarea 1---------")
print("La suma de la diagonal principal es:", sumarDiagonal(matriz))
print("¿El numero ", entero, "se encuentra en la matriz?", revisarEntero(matriz, entero))


