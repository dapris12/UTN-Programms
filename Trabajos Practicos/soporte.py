# Funciones
from math import e


def es_par(x):
    if x % 2 == 0:
        return True
    else:
        return False

def es_mayor(a, b, c):
    if b < a > c:
        return a
    elif a < b > c:
        return b
    else:
        return c

def es_menor(a, b, c):
    if b > a < c:
        return a
    elif a > b < c:
        return b
    else:
        return c

def duplex(pj,a,b,c,):
    dados = (a,b,c)
    d = dados[0] % 2
    e = dados[1] % 2
    f = dados[2] % 2
    if dados[0] == 0 and dados[1] == 0 and dados[2] == 0:
        pj = pj * 2
        return pj

def aveces(x,b):
    gano1 = gano2 = 0
    if x > b:
        gano1 += 1
        if gano2 >= 1:
            gano2 = 0

        if gano1 == 3:
            ganoseguidas1 = 1
            return ganoseguidas1
    else:
        gano2 += 1
        if gano1 >=1:
            gano1 = 0

        if gano2 == 3:
            ganoseguidas2 = 1
            return ganoseguidas2

def empate(x,b):
    empate = 0
    if x == b:
        empate = 1
        return empate

def promediojugadas(x,b):
    promedio = x*b/100
    return round(promedio , 2)

def aciertosparidad(x,b):
    promedio = x*b/100
    return round(promedio, 2)

def  empates(x,b):
    global jugador1_gana
    global jugador2_gana
    global empataron 

    jugador1_gana = jugador2_gana = 0
    if x > b:
        jugador1_gana += 1
        return jugador1_gana
    elif b > x:
        jugador2_gana += 1
        return jugador2_gana
    else:
        empataron = -1
        return empataron

def ganador():

    if jugador1_gana > jugador2_gana:
        return 1
    elif jugador2_gana > jugador1_gana:
        return 2
    else:
        return 0