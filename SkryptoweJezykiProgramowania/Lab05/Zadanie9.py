#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing

# stałe i zmienne globalne

# funkcje


def power_of_two_using_bit_shift(p: int) -> int:
    if p < 0:
        print("Potęgi liczb ujemnych nie są obsługiwane")
    return 1 << p


def main() -> None:
    try:
        exponent = int(input("Podaj wykładnik potęgi (p): "))
        result = power_of_two_using_bit_shift(exponent)
        print(f"2^{exponent} = {result}")
    except ValueError:
        print("Nieprawidłowe dane wejściowe.")


main()
