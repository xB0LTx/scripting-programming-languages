#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import datetime
import typing
# stałe i zmienne globalne

# funkcje


def data_roznica_dni(data1: datetime, data2: datetime) -> int:
    roznica = data2-data1
    roznica_dni = roznica.days
    return roznica_dni


def main() -> None:
    data1 = datetime.datetime(2023, 10, 10)
    data2 = datetime.datetime(2023, 12, 16)
    print(data_roznica_dni(data1, data2))


main()
