#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing

# stałe i zmienne globalne

# funkcje


def main() -> None:
    x = -1
    try:
        if x < 0:
            raise ValueError("Sorry, no numbers below zero")
    except ValueError as e:
        print(f"Caught an exception: {e}")


main()
