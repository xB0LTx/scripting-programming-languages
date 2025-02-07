#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing

# stałe i zmienne globalne

# funkcje

def main() ->  None:
    tuple = ("apple", "banana", "cherry")
    tuple_b = ("orange",)
    tuple += tuple_b  # dodawanie krotek
    multi_tuple = tuple * 2  # mnożenie krotek
    print(len(tuple))  # długość krotki - liczba elementów
    for x in tuple:  # wypisanie wszystkich elementów krotki
        print(x)


main()
"""a. Krotki tworzymy okrągłymi nawiasami, a po utworzeniu nie można modyfikować ich zawartości.
   b. Krotka zostanie powielona, zostaną do niej dopisane jej własne elementy i zwiększy swoją długość dwukrotne.
   c. Tak samo jak dodawanie; ilość powieleń krotki w samej sobie zależy od tego, przez jaką liczbę ją przemnożymy.
   d. Przecinek daje pythonowi informację, że tuple_b jest krotką, bez przecinka interpretuje jego zawartość jako string.
   e. Tak."""