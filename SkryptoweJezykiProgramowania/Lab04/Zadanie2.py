#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing

# stałe i zmienne globalne

# funkcje


class Vehicle:

    def __init__(self, owner: str, table: str):
        self.owner = owner
        self.table = table

    def get_owner(self) -> str:
        return self.owner

    def get_sound(self):
        print("vehicle's brum brum")


class Car(Vehicle):

    def get_sound(self) -> None:
        print("car's brum brum")


def main() -> None:
    vehi = Vehicle("Andrzej", "PY001KY")
    print(vehi.get_owner())
    vehi.get_sound()
    cr = Car("Marcin", "CB001KY")
    print(cr.get_owner())
    cr.get_sound()


main()

"""Dla instancji klasy Car() wykonuje się metoda get_sound zawarta w klasie Car(),
podobnie dla Vehicle() wykonuje się metoda get_sound zawarta w klasie Vehicle(). Metody get_owner nie dało się
wykonać dla klasy Vehicle(), ponieważ ta metoda należy do klasy Car(). 
Można to naprawić przenosząc metodę __init__ do klasy nadrzędnej Vehicle(), wraz z metodą get_owner."""