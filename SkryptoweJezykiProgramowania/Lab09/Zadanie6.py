#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import numpy as np
# stałe i zmienne globalne

# funkcje


def main() -> None:
    random_array = np.random.rand(10)
    print("Wylosowana tablica:")
    print(random_array)
    sorted_array_ascending = np.sort(random_array)
    print("\nTablica posortowana rosnąco:")
    print(sorted_array_ascending)
    sorted_array_descending = np.sort(random_array)[::-1]
    print("\nTablica posortowana malejąco:")
    print(sorted_array_descending)


main()
