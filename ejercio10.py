# -*- coding: utf-8 -*- 
# Decoración: Nombre del Algoritmo
print("-------------------------------------------------------")
print("Ejercicio 10: CALCULAR ÁREA Y VOLUMEN DEL CILINDRO.")
print("-------------------------------------------------------")

# Constantes
PI = 3.1416

# Entradas
print("Ingrese radio y alto: ")
radio = float(input("Radio: "))
alto = float(input("Alto: "))

# Proceso
volumen = PI * radio**2 * alto
area = 2 * PI * radio * (radio + alto)

# Salida
print("\nSALIDA:")
print("-------------------------------------------------------")
print(f"Volumen: {volumen:.2f}")
print(f"Área: {area:.2f}")
