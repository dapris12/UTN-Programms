import random
import soporte

# Inicializacion
jugador1 = input("Ingrese el nombre del Jugador 1: ")
jugador2 = input("Ingrese el nombre del Jugador 2: ")
objetivo = int(input("Ingrese el puntaje con el que se gana el juego: "))
while objetivo <= 10:
    objetivo = int(input("El puntaje ingresado debe ser mayor a 10: "))

puntaje_total1 = puntaje_total2 = puntaje_parcial1 = puntaje_parcial2 = cantidad_jugadas = aciertos_uno = aciertos_dos = 0

# Turnos
while puntaje_total1 < objetivo and puntaje_total2 < objetivo:
    print("Es el turno de", jugador1)
    apuesta1 = input("Ingrese su apuesta (Par o Impar): ")
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    dado3 = random.randint(1, 6)
    suma_dados1 = dado1 + dado2 + dado3
    dado_mayor = soporte.es_mayor(dado1, dado2, dado3)
    dado_menor = soporte.es_menor(dado1, dado2, dado3)

    if apuesta1 == "par" or apuesta1 == "PAR" or apuesta1 == "Par":
        if soporte.es_par(suma_dados1) == True:
            puntaje_parcial1 += dado_mayor
            print("mayor") #Cambiar
            aciertos_uno += 1
            soporte.duplex(puntaje_parcial1, dado1, dado2, dado3)
        else:
            puntaje_parcial1 -= dado_menor
            print("menor")

    else:
        if soporte.es_par(suma_dados1) == False:
            puntaje_parcial1 += dado_mayor
            print("mayor") #Cambiar
            aciertos_uno += 1
            soporte.duplex(puntaje_parcial1, dado1, dado2, dado3)
        else:
            puntaje_parcial1 -= dado_menor
            print("menor")

    puntaje_total1 = puntaje_total1 + puntaje_parcial1

    print("le tocaron los siguientes dados: ", dado1, dado2, dado3, "y la suma de ellos es de: ", suma_dados1)
    print(jugador1, "ha elegido", apuesta1, "y su puntaje parcial es de:", puntaje_parcial1, " ", puntaje_total1)

    print("Es el turno de", jugador2)
    apuesta1 = input("Ingrese su apuesta (Par o Impar): ")
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    dado3 = random.randint(1, 6)
    suma_dados1 = dado1 + dado2 + dado3
    dado_mayor = soporte.es_mayor(dado1, dado2, dado3)
    dado_menor = soporte.es_menor(dado1, dado2, dado3)
    if apuesta1 == "par" or apuesta1 == "PAR" or apuesta1 == "Par":
        if soporte.es_par(suma_dados1) == True:
            puntaje_parcial2 += dado_mayor
            aciertos_dos += 1
            print("mayor")
            soporte.duplex(puntaje_parcial1, dado1, dado2, dado3)
        else:
            puntaje_parcial2 -= dado_menor
            print("menor")
    else:
        if soporte.es_par(suma_dados1) == False:
            puntaje_parcial2 += dado_mayor
            aciertos_dos += 1
            print("mayor")
            soporte.duplex(puntaje_parcial1, dado1, dado2, dado3)
        else:
            puntaje_parcial2 -= dado_menor
            print("menor")

    puntaje_total2 = puntaje_total2 + puntaje_parcial2

    print("le tocaron los siguientes dados: ", dado1, dado2, dado3, "y la suma de ellos es de: ", suma_dados1)
    print(jugador2, "ha elegido", apuesta1, "y su puntaje parcial es de:", puntaje_parcial2, " ", puntaje_total2)
    empates = soporte.empates(puntaje_parcial1, puntaje_parcial2)

    cantidad_jugadas += 1
    empate = soporte.empate(puntaje_parcial1, puntaje_parcial2)
    aveces = soporte.aveces(puntaje_parcial1, puntaje_parcial2)

if puntaje_total1 > puntaje_total2:
    ganador = jugador1
elif puntaje_total2 > puntaje_total1:
    ganador = jugador2
else: 
    if soporte.ganador() == 1:
        ganador fue tutut
    elif soporte.ganador() == 2:
        ganador fue tata
    else:
        hubo empate

promediojugador1 = soporte.promediojugadas(puntaje_total1, cantidad_jugadas) #Jugador 1
promediojugador2 = soporte.promediojugadas(puntaje_total2, cantidad_jugadas) #Jugador 2

cantidad1 = soporte.aciertosparidad(aciertos_uno, cantidad_jugadas) #jugador1
cantidad2 = soporte.aciertosparidad(aciertos_dos, cantidad_jugadas) #jugador2

if cantidad1 > cantidad2:
    if ganador == jugador1:
        print ("si, si fue")
    else: 
        print("No no fue")



