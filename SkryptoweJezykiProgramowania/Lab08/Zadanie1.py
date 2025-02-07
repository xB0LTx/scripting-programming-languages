#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import re
# stałe i zmienne globalne

# funkcje


def main() -> None:
    import re
    text = 'aaaa'
    print("Kwantyfikator '+':", re.findall('a+', text))
    print("Kwantyfikator '+?':", re.findall('a+?', text))
    print("Kwantyfikator '*':", re.findall('a*', text))
    print("Kwantyfikator '*?':", re.findall('a*?', text))
    print("Kwantyfikator '?':", re.findall('a?', text))
    print("Kwantyfikator '??':", re.findall('a??', text))


main()
"""Kwantyfikator '+': ['aaaa'] - Dopasowuje jedno lub więcej wystąpień 'a'.

Kwantyfikator '+?': ['a', 'a', 'a', 'a'] - Leniwy odpowiednik '+', dopasowuje jak najmniejszą ilość 'a'.

Kwantyfikator '*': ['aaaa', ''] - Dopasowuje zero lub więcej wystąpień 'a'.

Kwantyfikator '*?': ['', 'a', 'a', 'a', 'a', ''] - Leniwy odpowiednik '*', dopasowuje jak najmniejszą ilość 'a'.

Kwantyfikator '?': ['a', 'a', 'a', 'a', ''] - Dopasowuje zero lub jedno wystąpienie 'a'.

Kwantyfikator '??': ['', 'a', '', 'a', '', 'a', '', 'a', ''] - Leniwy odpowiednik '?', dopasowuje jak najmniejszą ilość 'a'."""
