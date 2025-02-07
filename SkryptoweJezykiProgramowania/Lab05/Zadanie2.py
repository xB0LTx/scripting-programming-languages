#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing

# stałe i zmienne globalne

# funkcje


def get_bit_value(number: int, bit_index: int) -> int:
    if 0 <= number <= 255 and 0 <= bit_index < 8:
        bit_mask = 1 << bit_index
        bit_value = (number & bit_mask) >> bit_index
        return bit_value
    else:
        print("Podano nieprawidłowe wartości. Zakres liczb to 0-255, a indeks bitu od 0 do 7.")


def main() -> None:
    number = int(input("Podaj liczbę (0-255): "))
    bit_index = int(input("Podaj indeks bitu (0-7): "))
    result = get_bit_value(number, bit_index)
    if result is not None:
        print(f"Wartość bitu na bicie o indeksie {bit_index} to: {result}")


main()
