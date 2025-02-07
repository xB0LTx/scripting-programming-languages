#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import platform
import typing
# stałe i zmienne globalne

# funkcje


def wersja() -> None:
    ver = platform.python_version()
    print("Aktualnie wykorzystywana wersja Pythona: ", ver, "\n")


def main() -> None:
    wersja()


main()
