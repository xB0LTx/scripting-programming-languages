#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing

# stałe i zmienne globalne

# funkcje


def replace_dead_stops(file_path: str) -> None:
    with open(file_path, 'r', encoding='utf-8') as file:
        original_text = file.read()
    lines = original_text.split('\n')
    modified_lines = []
    for line in lines:
        words = line.split()
        modified_words = []
        for word in words:
            if '.' in word and '...' not in word:
                word = word.replace('.', '...')
            modified_words.append(word)
        modified_lines.append(' '.join(modified_words))
    modified_text = '\n'.join(modified_lines)
    print(modified_text)


def main() -> None:
    replace_dead_stops("inwokacja.txt")


main()
