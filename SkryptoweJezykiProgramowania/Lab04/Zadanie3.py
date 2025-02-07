#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
from random import randint
from typing import List

# stałe i zmienne globalne

# funkcje


class Student:
    quantity = 0

    def __init__(self):
        self.name = ""
        self.last_name = ""
        self.index = ""
        self.marks = []
        self.avg = float
        Student.quantity += 1

    def give_name(self, name: str, last_name: str) -> None:
        self.name = name
        self.last_name = last_name

    def give_index(self) -> None:
        self.index = str(randint(100000, 1000000))

    def give_mark(self, mark: int) -> None:
        self.marks.append(mark)

    def get_marks(self) -> List[int]:
        return self.marks

    def get_avg(self) -> float:
        amount = len(self.marks)
        sum_of_grades = 0
        for i in range(amount):
            sum_of_grades += self.marks[i]
        self.avg = sum_of_grades/amount
        return self.avg

    def say_hello(self) -> None:
        print("Hello! I'm " + self.name + " " + self.last_name + " " + self.index)


def main() -> None:
    a = Student()
    b = Student()
    c = Student()
    d = Student()
    e = Student()
    print(Student.quantity)


main()
"""Obiekty nie mają dostępu do zmiennej, ten ma jedynie klasa Student()"""