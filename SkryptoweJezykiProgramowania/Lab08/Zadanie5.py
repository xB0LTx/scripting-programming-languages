#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import re
# stałe i zmienne globalne

# funkcje


def main() -> None:
    print(re.match("[a-z]{3}", "Ala ma kota a kot ma Ale"))
    print(re.match("[a-z]{3}", "Ala ma kota a kot ma Ale", flags=re.I))


main()
"""Flaga re.I albo inaczej re.IGNORECASE pozwala na ignorowanie wielkości liter w dopasowaniach."""
