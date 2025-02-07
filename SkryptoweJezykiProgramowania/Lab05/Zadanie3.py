#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import random
# stałe i zmienne globalne

# funkcje


def calculate_triangle_area() -> tuple:
    side1 = random.randint(3, 10)
    side2 = random.randint(3, 10)
    side3 = random.randint(3, 10)
    if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
        perimeter = side1 + side2 + side3
        half_perimeter = perimeter / 2
        area = (half_perimeter * (half_perimeter - side1) * (half_perimeter - side2) * (half_perimeter - side3))**0.5
        return side1, side2, side3, area


def main() -> None:
    result = calculate_triangle_area()
    if result:
        side1, side2, side3, area = result
        print(f"Losowe boki trójkąta: {side1}, {side2}, {side3}")
        print(f"Pole trójkąta wynosi: {area:.2f}")
    else:
        print("Nie można utworzyć trójkąta z wylosowanych boków.")


main()
