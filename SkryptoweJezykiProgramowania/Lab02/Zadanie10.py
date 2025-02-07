#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
# stałe i zmienne globalne

# funkcje


def calc() -> None:
    a = input("Podaj pierwszą liczbę\n")
    b = input("Podaj drugą liczbę\n")
    a = float(a)
    b = float(b)
    dodawanie = a+b
    odejmowanie = a-b
    mnozenie = a*b
    dzielenie = a/b
    dzielenie_calk = a//b
    modulo = a % b
    potegowanie = a**b
    print("a+b = ", dodawanie, "\na-b = ", odejmowanie, "\na*b = ", mnozenie, "\na/b = ", dzielenie, "\na//b = ",
          dzielenie_calk, "\na%b = ", modulo, "\na**b = ", potegowanie, "\n")


def main():
    calc()


main()
