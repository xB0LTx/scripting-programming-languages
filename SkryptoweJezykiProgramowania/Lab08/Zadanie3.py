#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import re
# stałe i zmienne globalne

# funkcje


def main() -> None:
    with open('adresy.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    address_pattern = re.compile(
        r"ul\. (?P<street_name>[\w\s]+) (?:(?P<house_number>\d+)(?:/(?P<apartment_number>\d+))?)? (\d{2}-\d{3})")
    for line in lines:
        match = address_pattern.search(line)
        if match:
            street_name = match.group('street_name').strip()
            apartment_number = match.group('apartment_number').strip() if match.group('apartment_number') else "None"
            postal_code = match.group(4).strip()
            print(
                f"Nazwa ulicy: {street_name}, Numer mieszkania: {apartment_number}, Kod pocztowy: {postal_code}")


main()
