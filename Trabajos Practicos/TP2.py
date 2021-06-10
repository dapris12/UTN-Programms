# Functions

# Sumamos los resultados de los dados


def parity(a, b, c):
    summation = a + b + c
    return summation

# HIT PARITY | Comparamos si la suma de la misma es par o impar , luego revisamos si los N° de los dados son de la paridad elegida


def hit_parity(n, a, b, c):
    dices = (a, b, c)
    selection = input(
        "Ingrese si cree que el la sumatoria de estas sera PAR/IMPAR: ")
    while selection != "par" and selection != "impar" and selection != "PAR" and selection != "IMPAR":
        print("[Error] Debe ingresar PAR o IMPAR. (Intente no escribirlo todo en minusucla o mayuscula)")
        print("\n")
        selection = input(
            "Ingrese si cree que el la sumatoria de estas sera PAR/IMPAR: ")
    if selection == "par" or selection == "PAR":
        if n % 2 == 0:
            print("La paridad elegida fue correcta")
            d = dices[0] % 2
            e = dices[1] % 2
            f = dices[2] % 2

            if d == 0 and e == 0 and f == 0:
                print("Todos son pares")
            else:
                print("Son impares")
    else:
        if n % 2 == 1:
            print("La Paridad elegida fue correcta")
            d = dices[0] % 2
            e = dices[1] % 2
            f = dices[2] % 2

            if d == 0 and e == 0 and f == 0:
                print("Todos son impares")
            else:
                print("Todos no son impares")

# Contains all the fuctions calls
# all that mainline logic


def main():

    maxpj = int(input(
        "Ingrese el maximo de puntos que debera alcanzar un jugador para finalizar: "))

    # Random numbers Summation Replace numbers for random.range(x,x)
    dicesrandom = parity(2, 2, 4)
    hit_parity(dicesrandom, 2, 2, 4)
    print(dicesrandom)  # Print

# this is the starting point for the program


main()
print("func")

# definir variables | hit_parity - Selection parity(par,impar) summation % 2 == 0 Suma y duplicacion o resta, parity summation,  Most_Played(a,b),
# empated_playeds(a), avarage_per_play(a,b),avarge_per_hits(a,b),player_winn_three(a) || main()
