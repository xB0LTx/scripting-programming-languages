#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import numpy as np
# stałe i zmienne globalne

# funkcje


def main() -> None:
    array = np.random.randint(0, 11, size=(10, 10))
    print("Tablica:")
    print(array, "\n")
    numbers, counts = np.unique(array, return_counts=True)
    for number, count in zip(numbers, counts):
        print(f"Ilość wystąpień liczby {number}: {count}")


main()
