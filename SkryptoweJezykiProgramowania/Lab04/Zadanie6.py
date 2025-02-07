#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing

# stałe i zmienne globalne

# funkcje


class Vehicle:

    def __init__(self, owner: str, table: str):
        self.owner = owner
        self.table = table

    def __repr__(self) -> str:
        return self.owner + " " + self.table

    def __str__(self) -> str:
        return self.owner + " " + self.table

    def __eq__(self, o: object) -> bool:  # funkcja do sprawdzania równości (==)
        return self.owner == o.owner

    def __ne__(self, o: object) -> bool:  # funkcja zastępująca !=
        return self.owner != o.owner

    def __lt__(self, o: object) -> bool:  # funkcja zastępująca <
        return self.owner < o.owner

    def __gt__(self, o: object) -> bool:  # funkcja zastępująca >
        return self.owner > o.owner

    def __le__(self, o: object) -> bool:
        return self.owner <= o.owner

    def __ge__(self, o: object) -> bool:
        return self.owner >= o.owner

    def get_owner(self) -> str:
        return self.owner

    def get_sound(self):
        print("vehicle's brum brum")


class Car(Vehicle):

    def get_sound(self) -> None:
        print("car's brum brum")


def main() -> None:
    vehi = Vehicle("Andrzej", "PY001KY")
    cr = Car("Marcin", "CB001KY")
    print(vehi.__eq__(cr))
    print(vehi.__ne__(cr))
    print(vehi.__lt__(cr))
    print(vehi.__gt__(cr))
    print(vehi.__le__(cr))
    print(vehi.__ge__(cr))



main()

