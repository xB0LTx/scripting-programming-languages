#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import shutil


# stałe i zmienne globalne

# funkcje


def main() -> None:
    shutil.copy("test_file_a.txt", "../Lab05")
    shutil.copy("test_file_b.txt", "../Lab05")
    shutil.copy("test_file_b.txt", "../nieistnieje")


main()
