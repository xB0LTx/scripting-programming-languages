#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing

# stałe i zmienne globalne

# funkcje


class Vehicle:

    def __init__(self, owner: str, table: str):
        print("Vehicle constructor")
        self.owner = owner
        self.table = table

    def get_owner(self) -> str:
        return self.owner

    def get_sound(self):
        print("vehicle's brum brum")


class Car(Vehicle):

    def __init__(self, owner: str, table: str):
        print("Car constructor")
        self.table = table
        super().__init__(owner, table)

    def get_sound(self) -> None:
        print("car's brum brum")


def main() -> None:
    cr = Car("Marcin", "CB001KY")


main()
"""W klasie dziedziczącej, najpierw zostaje wywołany konstruktor własny, a potem konstrukor z klasy wyższej."""
