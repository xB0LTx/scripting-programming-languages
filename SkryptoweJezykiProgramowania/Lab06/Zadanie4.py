#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing

# stałe i zmienne globalne

# funkcje


def main() -> None:
    try:
        f = open("/sciezka/sciezka/plik.txt", "r")
        print(f.read())  # odczyt całego pliku do końca
        f = open("plik.txt", "r")
        print(f.readline())  # odczyt jednej linii
        f = open("plik.txt", "r")
        print(f.read(10))  # odczyt pierwszych 10 znaków
        f = open("thefile.txt", "r")
        for x in f:
            print(x)  # odczyt w pętli
        f = open("plik.txt", "r")
        list = f.readlines()  # wszystkie linie do listy
        list = f.readlines(10)  # 10 pierwszych do listy
        f.close()  # otwarte pliki należy zamykać
    except FileNotFoundError:
        print("Plik, który próbujesz otworzyć nie istnieje!")


main()
