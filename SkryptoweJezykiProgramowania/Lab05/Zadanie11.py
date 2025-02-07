#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import pytest
import math
# stałe i zmienne globalne

# funkcje


def calculate_ladder_height(length: float, angle_degrees: float) -> float:
    angle_radians = math.radians(angle_degrees)
    ladder_height = length * math.sin(angle_radians)
    return ladder_height


def test_calculate_ladder_height_positive_angle():
    result = calculate_ladder_height(5.0, 30.0)
    assert pytest.approx(result, 0.01) == 2.5


def test_calculate_ladder_height_zero_length():
    result = calculate_ladder_height(0.0, 45.0)
    assert "Nieprawidłowa długość drabiny bądź kąt"


def test_calculate_ladder_height_negative_length():
    result = calculate_ladder_height(-3.0, 60.0)
    assert "Nieprawidłowa długość drabiny bądź kąt"
