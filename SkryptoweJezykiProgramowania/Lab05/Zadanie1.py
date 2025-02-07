#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing

# stałe i zmienne globalne

# funkcje


def get_base() -> int:
    while True:
        try:
            base = int(input("Podaj podstawę systemu liczbowego (2, 8, 10 lub 16): "))
            if base in [2, 8, 10, 16]:
                return base
            else:
                print("Podana wartość nie jest prawidłową podstawą systemu liczbowego.")
        except ValueError:
            print("Podaj liczbę całkowitą (2, 8, 10 lub 16).")


def convert_number(number: str, base: int) -> str:
    if base == 2:
        return bin(number)
    elif base == 8:
        return oct(number)
    elif base == 10:
        return str(number)
    elif base == 16:
        return hex(number)


def main() -> None:
    base = get_base()
    number = input(f"Podaj liczbę w systemie o podstawie {base}: ")
    try:
        number = int(number, base)
        print(f"W postaci dwójkowej: {convert_number(number, 2)}")
        print(f"W postaci ósemkowej: {convert_number(number, 8)}")
        print(f"W postaci dziesiętnej: {convert_number(number, 10)}")
        print(f"W postaci heksadecymalnej: {convert_number(number, 16)}")
    except ValueError:
        print("Podana liczba nie jest prawidłowa w wybranym systemie liczbowym.")


main()
