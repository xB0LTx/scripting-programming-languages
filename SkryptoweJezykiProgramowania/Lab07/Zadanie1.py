#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
# stałe i zmienne globalne

# funkcje



def process_text(file_path: str) -> None:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    total_lines = len(lines)
    total_words = 0
    total_characters = 0
    for i, line in enumerate(lines, start=1):
        line = line.strip()
        num_characters = len(line)
        num_words = len(line.split())
        print(f"Wiersz {i}: Ilość znaków: {num_characters}, Ilość słów: {num_words}")
        total_words += num_words
        total_characters += num_characters
    print("\nIlość wierszy:", total_lines)
    print("Ilość wszystkich słów:", total_words)
    print("Ilość wszystkich znaków:", total_characters)


def main() -> None:
    process_text("inwokacja.txt")


main()
