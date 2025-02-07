#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
from Zadanie8 import random_numbers
# stałe i zmienne globalne

# funkcje


def main() -> None:
    n = 10  # Liczba losowych liczb do wygenerowania
    a = 1  # Dolna granica przedziału
    b = 100  # Górna granica przedziału
    filename = "random_numbers.txt"  # Nazwa pliku, w którym zostaną zapisane liczby
    random_numbers(n, a, b, filename)
    with open("random_numbers.txt", "r") as file:
        nums = file.readlines()
        file.close()
    for i in range(len(nums)):
        nums[i].strip()
        nums[i] = bin(int(nums[i]))
    with open("random_numbers_bin.txt", "w") as bin_file:
        for i in range(len(nums)):
            bin_file.write(f"{nums[i]}\n")


main()
