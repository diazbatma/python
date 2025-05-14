# -*- coding: utf-8 -*-
import math  # Librería necesaria para usar funciones Matemáticas, como math.ceil()

# Decoración: Nombre del Algoritmo
print("-------------------------------------------------------")
print("Ejercicio 5: NÚMERO DE MICRO DISCOS 3.5 NECESARIOS")
print("-------------------------------------------------------")

# Entradas
gigabytes = float(input("Ingrese cantidad de gigabytes: "))

# Proceso
megabytes = gigabytes * 1024  # 1 GB = 1024 MB
discosNecesarios = megabytes / 1.44  # Cada disquete almacena 1.44 MB

# Salida
print("\nSALIDA:")
print("-------------------------------------------------------")
print(f"Discos necesarios (número exacto): {discosNecesarios}")
print(f"Número de discos necesarios (redondeado al entero superior): {math.ceil(discosNecesarios)}")
