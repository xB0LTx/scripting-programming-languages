#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import numpy as np
# stałe i zmienne globalne

# funkcje


def replace_zeros(A, x):
    A[A == 0] = x
    return A


def main() -> None:
    matrix = np.array([[1, 0, 3], [0, 5, 0], [6, 7, 0]])
    print("Macierz pierwotna:")
    print(matrix)
    replacement_value = 10
    result_matrix = replace_zeros(matrix, replacement_value)
    print("\nMacierz po zamianie zer na ", replacement_value, ":")
    print(result_matrix)


main()
