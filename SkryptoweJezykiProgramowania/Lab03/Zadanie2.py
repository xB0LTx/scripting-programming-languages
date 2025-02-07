#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing

# stałe i zmienne globalne

# funkcje


def zadanie2() -> None:
    print("Zadanie 2\n")
    user_list = []
    for i in range(10):
        print("Podaj liczbę nr", i)
        user_number = int(input())
        user_list.append(user_number)
    print("Twoja lista\n", user_list)
    sorted_user_list = sorted(user_list)
    print("Największy element: ", sorted_user_list[9],
          "\nNajmniejszy element listy: ", sorted_user_list[0], "\n")
    non_negative_user_list = []
    for i in range(len(user_list)):
        if user_list[i] >= 0:
            non_negative_user_list.append(user_list[i])
    avg = sum(non_negative_user_list)/len(non_negative_user_list)
    print("Średnia liczb nieujemnych na liście: ", avg)


def main() -> None:
    zadanie2()


main()
