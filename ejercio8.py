# -*- coding: utf-8 -*-
# Decoración: Nombre del Algoritmo
print("-------------------------------------------------------")
print("Ejercicio 8: CALCULAR PERÍMETRO Y SUPERFICIE DEL RECTÁNGULO")
print("-------------------------------------------------------")

# Entradas
BASE = float(input("Ingrese la base: "))
ALTO = float(input("Ingrese el alto: "))

# Proceso
superficie = BASE * ALTO
perimetro = 2 * (BASE + ALTO)

# Salida
print("\nSALIDA:")
print("-------------------------------------------------------")
print(f"Superficie: {superficie}")
print(f"Perímetro: {perimetro}")
