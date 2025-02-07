#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import numpy as np
# stałe i zmienne globalne

# funkcje


def print_matrix_and_max_values(matrix):
    print("Macierz pierwotna:")
    print(matrix)
    global_max = np.max(matrix)
    print("\nElement największy globalnie:", global_max)
    row_max_values = np.max(matrix, axis=1)
    print("\nNajwiększy element w każdym wierszu:")
    print(row_max_values)
    col_max_values = np.max(matrix, axis=0)
    print("\nNajwiększy element w każdej kolumnie:")
    print(col_max_values)


def main() -> None:
    matrix_size = (10, 10)
    numbers = np.arange(0, 100, 1)
    matrix = np.reshape(numbers, matrix_size)
    print_matrix_and_max_values(matrix)


main()
