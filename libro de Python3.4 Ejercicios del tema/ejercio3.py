print("-------------------------------------------------------")
print("Ejercicio 3: PUNTAJE FINAL")
print("-------------------------------------------------------")

# Entradas
respuestasCorrectas = int(input("Ingrese número de respuestas correctas: "))
respuestasIncorrectas = int(input("Ingrese número de respuestas incorrectas: "))
respuestasEnBlanco = int(input("Ingrese número de respuestas en blanco: "))

# Proceso
puntajeRespuestasCorrectas = respuestasCorrectas * 3
puntajeRespuestasIncorrectas = respuestasIncorrectas * -1
puntajeRespuestasEnBlanco = respuestasEnBlanco * 0
puntajeFinal = puntajeRespuestasCorrectas + puntajeRespuestasIncorrectas + puntajeRespuestasEnBlanco

# Salida
print("-------------------------------------------------------")
print("El puntaje total es:", puntajeFinal)
print("-------------------------------------------------------")
