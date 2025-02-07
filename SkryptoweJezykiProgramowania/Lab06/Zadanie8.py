#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import random
# stałe i zmienne globalne

# funkcje


def random_numbers(n: int, a: int, b: int, filename: str) -> None:
    with open(filename, "w") as file:
        for i in range(n):
            random_number = random.randint(a, b)
            file.write(str(random_number) + "\n")


def main() -> None:
    n = 10
    a = 1
    b = 100
    filename = "random_numbers.txt"
    random_numbers(n, a, b, filename)
    #print(f"{n} losowych liczb z zakresu {a} - {b} zostało zapisanych do '{filename}'.")


main()
