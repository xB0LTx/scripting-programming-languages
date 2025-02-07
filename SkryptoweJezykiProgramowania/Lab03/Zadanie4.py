#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing

# stałe i zmienne globalne

# funkcje


def zadanie4() -> None:
    list_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_4_odd = []
    print("Zadanie4\nLista: ", list_4, "\n")
    for i in range(len(list_4)):
        if list_4[i] % 2 != 0:
            list_4_odd.append(list_4[i])
    sorted_list_4_odd = sorted(list_4_odd)
    print("Lista elementów nieparzystych: ", list_4_odd, "\nNajmniejszy element nieparzysty: ", sorted_list_4_odd[0])


def main() -> None:
    zadanie4()


main()
