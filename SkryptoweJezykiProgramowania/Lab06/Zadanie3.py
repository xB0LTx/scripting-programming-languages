#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing

# stałe i zmienne globalne

# funkcje


def main() -> None:
    try:
        a = 3*3
        if a != 9:
            raise ValueError("Coś poszło mocno nie tak!")
    except ValueError:
        print(f"{ValueError}")
    else:
        print("a = 3*3\na = 9")
    finally:
        print("Działanie zostało wykonane")


main()
