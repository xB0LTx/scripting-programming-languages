#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import re
# stałe i zmienne globalne

# funkcje


def process_strings(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    end_with_x_or_y = []
    three_chars_start_with_a = []
    starts_with_vowel = []
    for line in lines:
        line = line.strip()
        if re.search(r'[xy]$', line):
            end_with_x_or_y.append(line)
        if re.match(r'^a\w{2}$', line):
            three_chars_start_with_a.append(line)
        if re.match(r'^[aeiouyAEIOUY]', line):
            starts_with_vowel.append(line)
    print("Elements ending with x or y:")
    print(end_with_x_or_y)
    print("\nThree-character elements starting with a:")
    print(three_chars_start_with_a)
    print("\nElements starting with a vowel:")
    print(starts_with_vowel)


def main() -> None:
    file_path = 'napisy.txt'
    process_strings(file_path)


main()
