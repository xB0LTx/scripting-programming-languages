#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import math
# stałe i zmienne globalne

# funkcje


def calculate_ladder_height(length: float, angle_degrees: float) -> float or str:
    if length > 0 and angle_degrees >= 0:
        angle_radians = math.radians(angle_degrees)
        ladder_height = length * math.sin(angle_radians)
        return ladder_height
    else:
        return "Nieprawidłowa długość drabiny bądź kąt"


def main() -> None:
    length = float(input("Podaj długość drabiny: "))
    angle_degrees = float(input("Podaj kąt drabiny względem poziomu (w stopniach): "))
    ladder_height = calculate_ladder_height(length, angle_degrees)
    print(f"Wysokość, na jaką sięga koniec drabiny, wynosi: {ladder_height:.2f}")


main()
