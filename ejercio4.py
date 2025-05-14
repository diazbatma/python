# Decoración: Nombre del Algoritmo 
print("-------------------------------------------------------")
print("Ejercicio 4: PUNTAJE TOTAL DE PARTIDOS.")
print("-------------------------------------------------------")

# Entradas
PG = int(input("Ingrese número de partidos ganados: "))
PE = int(input("Ingrese número de partidos empatados: "))
PP = int(input("Ingrese número de partidos perdidos: "))

# Proceso
PF = (PG * 3) + (PE * 1)  # partidos perdidos no suman puntos, no es necesario agregarlos

# Salida
print("\nSALIDA:")
print("-------------------------------------------------------")
print("Puntaje Final:", PF)
