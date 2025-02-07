#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import numpy as np
# stałe i zmienne globalne

# funkcje


def reshape_test(matrix, shape1, shape2):
    matrix_backup = matrix
    print("Macierz pierwotna:")
    print(matrix)
    reshaped_matrix1 = np.reshape(matrix, (shape1, -1))
    print("\nMacierz po użyciu reshape z liczbą -1 jako pierwszym parametrem:")
    print(reshaped_matrix1)
    reshaped_matrix2 = np.reshape(matrix_backup, (-1, shape2))
    print("\nMacierz po użyciu reshape z liczbą -1 jako drugim parametrem:")
    print(reshaped_matrix2)


def main() -> None:
    original_matrix = np.array([[1, 2, 3], [4, 5, 6]])
    reshape_test(original_matrix, 3, 3)


main()
"""Parametr -1 wskazuje, że ta wymiarowa wartość powinna być automatycznie obliczona na podstawie rozmiaru oryginalnej 
macierzy i innych wymiarów, aby zachować spójność danych."""
