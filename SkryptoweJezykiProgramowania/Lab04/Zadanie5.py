#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing

# stałe i zmienne globalne

# funkcje


class Item:

    def get_sound(self) -> None:
        print("item's sound")


class Element:
    def get_sound(self) -> None:
        print("element's sound")


class Thing(Item, Element):
    def say_hello(self) -> None:
        print("hello!")


def main() -> None:
    it = Item()
    el = Element()
    th = Thing()
    it.get_sound()
    el.get_sound()
    th.get_sound()


main()
"""Różnica polega na tym, że klasa Thing() będzie dziedziczyła atrybuty od klasy wymienionej jako pierwsza. """
