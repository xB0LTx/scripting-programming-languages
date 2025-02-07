#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import re
# stałe i zmienne globalne

# funkcje


def read_phone_numbers(file_path: str) -> list:
    with open(file_path, 'r', encoding='utf-8') as file:
        numbers = [line.strip() for line in file.readlines()]

    return numbers


def validate_phone_numbers(numbers: list) -> dict:
    validation_patterns = {
        "1. xxx-xxx-xxx": r'^\d{3}-\d{3}-\d{3}$',
        "2. xxxxxxxxx": r'^\d{9}$',
        "3. +48xxxxxxxxx": r'^\+48\d{9}$',
        "4. 0048xxxxxxxxx": r'^0048\d{9}$',
        "5. +48 xxx xxx xxx": r'^\+48\s\d{3}\s\d{3}\s\d{3}$',
    }
    counts = {key: 0 for key in validation_patterns}
    for number in numbers:
        for pattern_description, pattern in validation_patterns.items():
            if re.match(pattern, number):
                counts[pattern_description] += 1
                break
    return counts


def main() -> None:
    file_path = 'numery.txt'
    phone_numbers = read_phone_numbers(file_path)
    counts = validate_phone_numbers(phone_numbers)
    print("Ilość numerów telefonu o danym formacie:")
    for pattern_description, count in counts.items():
        print(f"{pattern_description}: {count} numery")


main()
