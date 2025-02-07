#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing

# stałe i zmienne globalne

# funkcje


def ppunkta() -> None:
    if 2 * 3 / 4 == 1.5:
        print("a) Mnożenie i dzielenie wykonuje się od lewej strony\n")
    else:
        print("a) Mnożenie i dzielenie wykonuje się od prawej strony\n")


def ppunktb() -> None:
    if 2 + 3 * 4 == 14 and 2 * 3 + 4 == 10:
        print("b) Mnożenie wykona się wcześniej\n")
    else:
        print("b) Mnożenie i dodawanie są równe i wykonują się od lewej strony\n")


def ppunktc() -> None:
    print("c) 2*2/4*4=", 2*2/4*4, "\n")
    print("(2*2)/(4*4)=", (2*2)/(4*4), "\n")
    print("Nawiasy wpływają na kolejność wykonywania działań, nawiasy wykonują się w kolejności od lewej do prawej "
          "i mają priorytet nad wszystkim innymi działaniami\n")


def ppunktd() -> None:
    if 2 * 2 ** 5 == 64:
        print("d) Potęgowanie jest ważniejsze od mnożenia")
    else:
        print("d) Mnożenie jest tak samo ważne jak potęgowanie")


def main() -> None:
    ppunkta()
    ppunktb()
    ppunktc()
    ppunktd()


main()
