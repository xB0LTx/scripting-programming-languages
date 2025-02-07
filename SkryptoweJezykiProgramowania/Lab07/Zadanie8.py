#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import re
# stałe i zmienne globalne

# funkcje


def validate_date(input_date: str) -> None:
    date_pattern = re.compile(r'^(0[1-9]|[12][0-9]|3[01])[-/](0[1-9]|1[0-2])[-/](\d{4})$')
    match = re.match(date_pattern, input_date)

    if match:
        day, month, year = map(int, match.groups())
        if 1 <= day <= 31 and 1 <= month <= 12:
            months = [
                "Styczeń", "Luty", "Marzec", "Kwiecień",
                "Maj", "Czerwiec", "Lipiec", "Sierpień",
                "Wrzesień", "Październik", "Listopad", "Grudzień"
            ]
            print(f"Miesiąc dla podanej daty: {months[month - 1]}")
        else:
            print("Niepoprawna ilość dni lub miesięcy")
    else:
        print("Niepoprawny format daty")


def main() -> None:
    user_input = input("Proszę wpisać datę (przyjmowane formaty to dd-mm-rrrr or dd/mm/rrrr): ")
    validate_date(user_input)


main()
