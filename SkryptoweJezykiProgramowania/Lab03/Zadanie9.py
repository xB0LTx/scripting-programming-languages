#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing

# stałe i zmienne globalne

# funkcje


def zadanie9() -> None:
    this_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
    the_set = {7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}
    print("Zadanie 9\na) ", the_set.isdisjoint(this_set), type(the_set.isdisjoint(this_set)),
          "\nb) ", the_set.issubset(this_set), type(the_set.issubset(this_set)),
          "\nc) ", the_set.issuperset(this_set), type(the_set.issuperset(this_set)),
          "\nd) ", the_set.union(this_set), type(the_set.union(this_set)),
          "\ne) ", the_set.difference(this_set), type(the_set.difference(this_set)),
          "\nf) ", the_set.intersection(this_set), type(the_set.intersection(this_set)))


def main() -> None:
    zadanie9()


main()
