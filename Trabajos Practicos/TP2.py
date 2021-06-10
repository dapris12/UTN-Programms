# Functions
def parity(a, b, c):
    summation = a + b + c
    return summation

# Contains all the fuctions calls
# all that mainline logic


def hit_parity(n, a, b, c):
    dices = [a, b, c]
    selection = input(
        "Ingrese si cree que el la sumatoria de estas sera PAR/IMPAR: ")
    while selection != "par" and selection != "impar" and selection != "PAR" and selection != "IMPAR":
        print("[Error] Debe ingresar PAR o IMPAR. (Intente no escribirlo todo en minusucla o mayuscula)")
        selection = input(
            "Ingrese si cree que el la sumatoria de estas sera PAR/IMPAR: ")
    if selection == "par" or selection == "PAR":
        if n % 2 == 0:
            print("La paridad elegida fue correcta")


def main():
    dicesrandom = parity(2, 2, 4)
    hit_parity(dicesrandom, 2 , 2, 4)
    print(dicesrandom)

# this is the starting point for the


main()
print("func")

# definir variables | hit_parity - Selection parity(par,impar) summation % 2 == 0 Suma y duplicacion o resta, parity summation,  Most_Played(a,b),
# empated_playeds(a), avarage_per_play(a,b),avarge_per_hits(a,b),player_winn_three(a) || main()
