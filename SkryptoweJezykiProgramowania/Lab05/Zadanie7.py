#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import math
# stałe i zmienne globalne

# funkcje


def main() -> None:
    for angle_degrees in range(91):
        angle_radians = math.radians(angle_degrees)
        sin_alfa = math.sin(angle_radians)
        cos_alfa = math.cos(angle_radians)
        if pow(sin_alfa, 2)+pow(cos_alfa, 2) != 1:
            print(f"Równanie nie zostało spełnione dla kąta {angle_degrees}.")
        elif angle_degrees == 90:
            print("Koniec sprawdzania.")


main()
