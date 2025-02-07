#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import re
import os
# stałe i zmienne globalne

# funkcje


def list_txt_files(directory_path: str) -> None:
    txt_files_pattern = re.compile(r'.*\.txt$', re.IGNORECASE)
    txt_files = [file for file in os.listdir(directory_path) if re.match(txt_files_pattern, file)]
    if txt_files:
        print(f"Pliki tekstowe w katalogu {directory_path}:")
        for txt_file in txt_files:
            print(txt_file)
    else:
        print(f"W katalogu {directory_path} nie znaleziono żadnych plików tekstowych.")


def main() -> None:
    directory_path = input("Wprowadź ścieżkę dostępu: ")
    if os.path.isdir(directory_path):
        list_txt_files(directory_path)
    else:
        print(f"{directory_path} nie jest poprawną ścieżką dostępu.")


main()
