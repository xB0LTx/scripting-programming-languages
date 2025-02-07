#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing

# stałe i zmienne globalne

#funkcje


def dwainty() -> None:
    a = 4/2
    print("a) ", type(a))


def intfloat() -> None:
    b = 4/2.5
    print("b) ", type(b))


def dwafloaty() -> None:
    c = 4.5/2.5
    print("c) ", type(c))

def main() -> None:
    dwainty()
    intfloat()
    dwafloaty()


main()
