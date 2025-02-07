#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import datetime
import typing
# stałe i zmienne globalne

# funkcje


def dataczas_mdy() -> str:
    now = datetime.datetime.now()
    data_czas1 = now.strftime("%m.%d.%Y  %H:%M:%S")
    return data_czas1


def dataczas_dmy() -> str:
    now = datetime.datetime.now()
    data_czas2 = now.strftime("%d.%m.%Y  %H:%M:%S")
    return data_czas2


def dataczas_ymd() -> str:
    now = datetime.datetime.now()
    data_czas3 = now.strftime("%Y.%m.%d  %H:%M:%S")
    return data_czas3


def main() -> None:
    print(dataczas_dmy(), "\n", dataczas_mdy(), "\n", dataczas_ymd())


main()
