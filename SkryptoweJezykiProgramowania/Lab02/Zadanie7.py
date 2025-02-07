#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
from math import sqrt, pow
# stałe i zmienne globalne

# funkcje


def delta(a: float, b: float, c: float) -> float:
    d = pow(b, 2) - 4 * a * c
    return d


def pierwiastki_rownania_kwadratowego(a: float, b: float, d: float) -> tuple:
    pierwiastek1 = (-b-sqrt(d))/(2*a)
    pierwiastek2 = (-b+sqrt(d))/(2*a)
    return pierwiastek1, pierwiastek2


def main() -> None:
    a = float(input("Podaj wartość a równania\n"))
    b = float(input("Podaj wartość b równania\n"))
    c = float(input("Podaj wartość c równania\n"))
    odp = pierwiastki_rownania_kwadratowego(a, b, delta(a, b, c))
    print("Podane równanie ma dwa rozwiązania:\nx1 = ", odp[0], "\nx2 = ", odp[1])


main()
