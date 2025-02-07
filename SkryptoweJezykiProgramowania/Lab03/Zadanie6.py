#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing

# stałe i zmienne globalne

# funkcje


def zadanie6() -> str:
    num_list = []
    while True:
        num = int(input("Podaj liczbę (0 kończy wprowadzanie): "))
        if num == 0:
            break
        elif num_list.count(num) == 0:
            num_list.append(num)
        else:
            for i in range(num_list.count(num)):
                num_list.remove(num)
    unique_elements = set(num_list)
    print(f"Unikatowe elementy listy: {unique_elements}")


def main() -> None:
    zadanie6()


main()
