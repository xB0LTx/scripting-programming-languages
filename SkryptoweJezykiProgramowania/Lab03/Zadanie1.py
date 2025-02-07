#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing

# stałe i zmienne globalne
my_list = ["one", "two", "three"]
# funkcje


def zadanie1a(a_list: list) -> None:
    print("Zadanie 1 a)\n")
    print(a_list, "\n")


def zadanie1b(b_list: list) -> list:
    for i in range(5):
        b_list.append(i)
    print("\n")
    return b_list


def zadanie1c(c_list: list) -> None:
    print("Zadanie 1 c)\n")
    for i in range(2):
        print(c_list[i])
    print("\n")
    for i in range(len(c_list)-1, len(c_list)-3, -1):
        print(c_list[i])
    print("\n")


def zadanie1d(d_list: list) -> None:
    print("Zadanie 1 d)\n")
    print(len(d_list), "\n")


def zadanie1e(e_list: list) -> None:
    print("Zadanie 1 e)\n")
    for i in range(0, len(e_list), 2):
        print(e_list[i])
    print("\n")


def zadanie1f(f_list: list) -> None:
    f_list.append(10)


def zadanie1g(g_list: list) -> None:
    g_list.append("napis")


def zadanie1h(h_list: list) -> None:
    print("Zadanie 1 h)\nLista przed posortowaniem\n", h_list)
    sorted(h_list)
    print("Lista po posortowaniu\n", h_list, "\n")


def zadanie1i(i_list: list) -> list:
    del i_list[-1]
    return i_list


def zadanie1j(j_list: list) -> None:
    print("Zadanie 1 j)\nLista przed posortowaniem\n", j_list)
    sorted(j_list, reverse=True)
    print("Lista po posortowaniu\n", j_list, "\n")


def zadanie1k(k_list: list) -> list:
    k_list.insert(2, "2")
    return k_list


def zadanie1l(l_list: list) -> None:
    print("Zadanie 1 l)\n")
    counter_13 = 0
    for i in range(len(l_list)):
        if l_list[i] == 13:
            counter_13 += 1
    print("Na liście występuje ", counter_13, " elementów o wartości 13\n")


def main() -> None:
    zadanie1a(my_list)
    zadanie1b(my_list)
    zadanie1c(my_list)
    zadanie1d(my_list)
    zadanie1e(my_list)
    zadanie1f(my_list)
    zadanie1g(my_list)
    #zadanie1h(my_list)
    zadanie1i(my_list)
    #zadanie1j(my_list)
    zadanie1k(my_list)
    zadanie1l(my_list)
"""a.Nie, ponieważ nie da się sortować list zawierających typy numeryczne i znakowe jednocześnie.
   b.W pythonie listy są numerowane od indeksu 0."""

main()
