#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
from math import pi
import typing
# stałe i zmienne globalne

# funkcje


def promien() -> float:
    print("Podaj promień koła:")
    r = float(input())
    return r


def obwod_kola(r: float) -> float:
    obw_kol = 2*pi*r
    return obw_kol


def pole_kola(r: float) -> float:
    pol_kol = pi * r ** 2
    return pol_kol


def main() -> None:
    r = promien()
    print("Obwód koła dla podanego promienia wynosi: ", obwod_kola(r), ", natomiast jego pole wynosi: ",
          pole_kola(r))


main()
