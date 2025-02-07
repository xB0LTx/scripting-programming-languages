#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing

# stałe i zmienne globalne

# funkcje


def zadanie3() -> None:
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [1, 3, 5, 7, 9]
    list_1_unique = []
    for i in range(len(list_1)):
        for j in range(len(list_2)):
            if list_1[i] == list_2[j]:
                break
            elif j == 4:
                list_1_unique.append(list_1[i])
    print("Zadanie3\nLista 1: ", list_1, "\nLista 2: ", list_2, "\nUnikalne elementy listy 1: ", list_1_unique)


def main() -> None:
    zadanie3()


main()
