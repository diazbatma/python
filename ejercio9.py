# -*- coding: utf-8 -*-
# Decoración: Nombre del Algoritmo 
print("-------------------------------------------------------")
print("Ejercicio 9: GASOLINERA")
print("-------------------------------------------------------")

# Constantes
LITXG = 3.785     # Litros por galón
PRECIOXL = 4.50   # Precio por litro en dólares

# Entrada
consumo_galones = float(input("Ingresar consumo en galones: "))

# Proceso
total = consumo_galones * LITXG * PRECIOXL

# Salida
print("\nSALIDA:")
print("-------------------------------------------------------")
print(f"Total a pagar: ${total:.2f}")
