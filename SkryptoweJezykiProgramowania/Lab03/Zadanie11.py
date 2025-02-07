#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing

# stałe i zmienne globalne

# funkcje


def zadanie11() -> None:
    grade_sheet = {
        "123456": {
            "name": "Jan",
            "family_name": "Kowalski",
            "grades": [4.5, 3.0, 5.0, 4.5, 3.5]
        },
        "234567": {
            "name": "Anna",
            "family_name": "Nowak",
            "grades": [4.0, 4.5, 3.5, 4.0, 5.0]
        },
        "345678": {
            "name": "Piotr",
            "family_name": "Wójcik",
            "grades": [3.0, 3.5, 4.0, 4.5, 3.5]
        }
    }

    for student_index, student in grade_sheet.items():
        name = student["name"]
        family_name = student["family_name"]
        grades = student["grades"]
        grade_avg = sum(grades) / len(grades)
        print("Studenci:\n")
        print(f"Numer indeksu: {student_index}")
        print(f"Imię: {name}")
        print(f"Nazwisko: {family_name}")
        print(f"Średnia ocen: {grade_avg:.2f}")
        print()


def main() -> None:
    zadanie11()


main()
