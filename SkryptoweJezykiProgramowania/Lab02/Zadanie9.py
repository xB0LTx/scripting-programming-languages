#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import calendar
import typing
# stałe i zmienne globalne

# funkcje


def generuj_kalendarz(rok: int, miesiac: int) -> calendar:
    try:
        kalendarz = calendar.month(rok, miesiac)
        return kalendarz
    except IndexError:
        return "Błąd: Nieprawidłowy rok lub miesiąc"


def main() -> None:
    rok = int(input("Podaj rok: "))
    miesiac = int(input("Podaj miesiąc (1-12): "))
    kalendarz = generuj_kalendarz(rok, miesiac)
    print(f"Kalendarz dla {miesiac}.{rok}:\n")
    print(kalendarz)


main()
