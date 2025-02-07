#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
from random import randint
from typing import List

# stałe i zmienne globalne

# funkcje


class Student:
    def __init__(self, name: str, last_name: str, index: int):
        self.name = name
        self.last_name = last_name
        self.index = index

    def __repr__(self) -> str:
        return self.name + " " + self.last_name

    def __str__(self) -> str:
        return self.last_name + " " + self.name

    def __eq__(self, o: object) -> bool: #funkcja do sprawdzania równości (==)
        return self.index == o.index

    def __ne__(self, o: object) -> bool: #funkcja zastępująca !=
        return self.index != o.index

    def __lt__(self, o: object) -> bool: #funkcja zastępująca <
        return self.index < o.index

    def __gt__(self, o: object) -> bool: #funkcja zastępująca >
        return self.index > o.index


s1 = Student('Joe', 'Doe', 111111)
s2 = Student('Jane', 'Key', 222222)
print(s1.__dict__)

"""Funkcja __dict__ przekształca obiekt klasa na słownik."""
