#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import numpy as np
# stałe i zmienne globalne

# funkcje


def main() -> None:
    matrix = np.random.rand(5, 5)
    weights = np.array([1, 2, 3, 2, 1])
    weighted_average = np.average(matrix, axis=1, weights=weights)
    print("Macierz:")
    print(matrix)
    print("\nŚrednia ważona dla każdego wiersza:")
    print(weighted_average)


main()
