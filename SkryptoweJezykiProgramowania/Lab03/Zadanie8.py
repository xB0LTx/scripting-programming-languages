#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing

# stałe i zmienne globalne

# funkcje


def zadanie8() -> None:
    the_set = {"orange", "lychee", "watermelon", "avocado", "tomato"}  # definiowanie zbioru
    print("Zadanie8\nZbiór początkowy")
    the_set.remove("watermelon")
    the_set.discard("orange")
    print("\na) po usuwaniu metodami remove i discard: ", the_set)
    x = the_set.pop() # wyjęcie ze zbioru jakiegoś elementu
    print("\nb) metoda pop: ", x, "\nlista:\n", the_set)
"""Metody z zadania a) usuwają tylko istniejące elementy,
zwracają błąd przy próbie usunięcia nieistniejącego elementu oraz psują wynik końcowy programy.
Metoda z zadania b), pop(), usuwa zawsze inny element zbioru, jeśli nie podamy żadnego indeksu"""


def main() -> None:
    zadanie8()


main()
