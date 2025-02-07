#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import numpy as np
# stałe i zmienne globalne

# funkcje


def main() -> None:
    array1 = np.array([[1, 2], [3, 4]])
    array2 = np.array([[5, 6], [7, 8]])
    star_operator = array1 * array2
    print("*:")
    print(star_operator)
    asterisk_operator = array1 @ array2
    print("\n@:")
    print(asterisk_operator)


main()
"""Operator * jest używany do mnożenia element-wise, co oznacza, że każdy odpowiadający sobie element w dwóch macierzach 
jest mnożony przez siebie.
Operator @ jest używany do mnożenia macierzowego, co oznacza, że wykonuje iloczyn skalarny, a wynikowa macierz zawiera 
sumy iloczynów odpowiednich elementów."""
