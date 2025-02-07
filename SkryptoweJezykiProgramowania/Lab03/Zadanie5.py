#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing

# stałe i zmienne globalne

# funkcje


def zadanie5() -> None:
    list_A = ["A", "B", "C"]
    list_B = ["D", "E", "F"]
    list_A += list_B
    print("Zadanie5\na) ", list_A)
    list_A = list_A[0:3:1]
    list_A = list_B+list_A
    print("\nb) ", list_A)


def main() -> None:
    zadanie5()


main()
