import random

print("¡Bienvenido al juego de Adivina el Número!")
print("Estoy pensando en un número del 1 al 100...")

numero_secreto = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input("Adiviná el número: "))
    intentos += 1

    if intento < numero_secreto:
        print("Demasiado bajo. Probá con un número más grande.")
    elif intento > numero_secreto:
        print("Demasiado alto. Probá con un número más chico.")
    else:
        print(f"¡Felicitaciones! Adivinaste el número en {intentos} intentos.")
        break