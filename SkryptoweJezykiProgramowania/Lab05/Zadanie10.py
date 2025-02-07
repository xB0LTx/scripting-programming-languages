#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import math
import sys
# stałe i zmienne globalne

# funkcje


def main() -> None:
    a = float(input("Podaj liczbę zmiennoprzecinkową (a): "))
    print(f"Math.trunc(a): {math.trunc(a)}")
    print(f"Math.floor(a): {math.floor(a)}")
    print(f"Math.ceil(a): {math.ceil(a)}")
    print(f"Math.fabs(a): {math.fabs(a)}")
    if sys.version_info >= (3, 9):
        b = float(input("Podaj drugą liczbę zmiennoprzecinkową (b): "))
        print(f"Math.lcm(a, b): {math.lcm(math.ceil(a), math.ceil(b))}")
        print(f"Math.gcd(a, b): {math.gcd(math.ceil(a), math.ceil(b))}")


main()
