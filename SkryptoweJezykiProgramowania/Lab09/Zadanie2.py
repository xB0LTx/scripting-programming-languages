#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import numpy as np
# stałe i zmienne globalne

# funkcje


def medianize(A):
    mean_value = np.mean(A)
    medianized_array = A - mean_value
    return medianized_array


def main() -> None:
    input_array = np.array([1, 2, 3, 4, 5])
    result_array = medianize(input_array)
    print("Tablica pierwotna:")
    print(input_array)
    print("\nTablica po użyciu funkcji medianize:")
    print(result_array)


main()
