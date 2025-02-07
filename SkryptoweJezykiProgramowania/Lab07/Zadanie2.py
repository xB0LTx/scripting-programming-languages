#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing

# stałe i zmienne globalne

# funkcje


def count_whitespaces(file_path: str) -> None:
    with open(file_path, 'r', encoding='utf-8') as file:
        file_text = file.read()
    num_newlines = file_text.count('\n')
    num_spaces = file_text.count(' ')
    num_tabs = file_text.count('\t')
    print("Number of newlines:", num_newlines)
    print("Number of spaces:", num_spaces)
    print("Number of tabs:", num_tabs)


def main() -> None:
    count_whitespaces("inwokacja.txt")


main()
