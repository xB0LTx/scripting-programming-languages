#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import re
# stałe i zmienne globalne

# funkcje


def main() -> None:
    with open('../Lab07/inwokacja.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    words_before_exclamation = re.findall(r'\b\w+\b(?=\s*!)', text)
    print("Słowa po których występuje '!':", words_before_exclamation)
    words_with_polish_chars = re.findall(r'\b\w*[ąćęłńóśźż]\w*\b', text)
    print("Słowa z polskimi znakami:", words_with_polish_chars)
    count_ci = len(re.findall(r'\bcię\b|\bci\b', text, flags=re.IGNORECASE))
    print("Liczba wystąpień 'cię' lub 'ci':", count_ci)


main()
