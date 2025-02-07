#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import os
# stałe i zmienne globalne

# funkcje


def tree(directory: str, indent="") -> None:
    if os.path.isdir(directory):
        print(indent + os.path.basename(directory) + "/")
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                tree(item_path, indent + "  ")
            else:
                print(indent + "  " + item)


def main() -> None:
    target_directory = input("Podaj ścieżkę katalogu, dla którego chcesz wyświetlić drzewo katalogów: ")
    tree(target_directory)


main()
