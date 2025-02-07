#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import re
# stałe i zmienne globalne

# funkcje


def validate_password(password):
    # Słabe hasło: Minimum 8 znaków
    weak_pattern = re.compile(r'^.{8,}$')
    # Średnie hasło: Minimum 8 znaków, przynajmniej jedna duża litera, jedna mała litera i jedna cyfra
    medium_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$')
    # Mocne hasło: Minimum 10 znaków, przynajmniej jedna duża litera, jedna mała litera, jedna cyfra i jeden znak specjalny
    strong_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W).{10,}$')
    if strong_pattern.match(password):
        return "Password is strong"
    elif medium_pattern.match(password):
        return "Password is medium"
    elif weak_pattern.match(password):
        return "Password is weak"
    else:
        return "Password does not meet the criteria for weak, medium, or strong"


def main() -> None:
    password1 = "weakPass"
    password2 = "MediumPass1"
    password3 = "Strong@Pass123"
    print(validate_password(password1))
    print(validate_password(password2))
    print(validate_password(password3))


main()
