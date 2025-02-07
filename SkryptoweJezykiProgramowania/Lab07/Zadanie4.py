#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import re
# stałe i zmienne globalne

# funkcje


def find_female_names(file_path: str) -> None:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    pattern = r'\b[A-Z][a-z]*a\b'
    female_names = re.findall(pattern, text)
    print(f"Damskie imiona znalezione w pliku: {file_path}")
    for name in female_names:
        print(name)


def main() -> None:
    find_female_names("imiona.txt")


main()
