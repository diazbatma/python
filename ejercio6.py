# -*- coding: utf-8 -*-
import math  # Necesario para usar math.sqrt()

# Decoración: Nombre del Algoritmo
print("-------------------------------------------------------")
print("Ejercicio 6: DISTANCIA ENTRE 2 PUNTOS A y B, en 2D.")
print("-------------------------------------------------------")

# Entradas
print("Ingrese coordenadas del Punto A: ")
AX = float(input("Ax: "))
AY = float(input("Ay: "))
print("Ingrese coordenadas del Punto B: ")
BX = float(input("Bx: "))
BY = float(input("By: "))

# Proceso
distancia = math.sqrt((AX - BX)**2 + (AY - BY)**2)

# Salida
print("\nSALIDA:")
print("-------------------------------------------------------")
print("Resultado:", distancia)
