#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import numpy as np
# stałe i zmienne globalne

# funkcje


def main() -> None:
    array = np.array([1.123456789, 2.345678901, 3.987654321])
    print("Domyślne opcje wyświetlania:")
    print(array)
    np.set_printoptions(precision=4)
    print("\nPrzykładowo dostosowane opcje wyświetlania (4 miejsca po przecinku):")
    print(array)


main()
"""Funkcja set_printoptions w bibliotece NumPy umożliwia dostosowanie sposobu, w jaki tablice NumPy są wyświetlane."""
