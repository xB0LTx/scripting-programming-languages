#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import numpy as np
# stałe i zmienne globalne

# funkcje


def main() -> None:
    grades_data = np.genfromtxt('oceny.csv', delimiter='\t', skip_header=1)
    min_lab_grades = np.min(grades_data[:, :5], axis=1)
    print("Najniższa ocena z laboratoriów dla każdego studenta:")
    print(min_lab_grades)
    avg_exam_grade = np.mean(grades_data[:, 5])
    print("Średnia ocena z egzaminu:", avg_exam_grade)
    num_2_exam_grades = np.sum(grades_data[:, 5] == 2)
    print("liczba 2 z egzaminu:", num_2_exam_grades)
    has_all_5_lab_grades = np.any(np.all(grades_data[:, :5] == 5, axis=1))
    print("Czy jest student, który miał same 5 z laboratoriów?:", has_all_5_lab_grades)
    has_2_in_lab2_and_lab3 = np.any((grades_data[:, 1] == 2) & (grades_data[:, 2] == 2))
    print("Czy jest student, który miał 2 z LAB2 i LAB3?:", has_2_in_lab2_and_lab3)
    students_higher_exam_than_avg_lab = np.sum(grades_data[:, 5] > avg_exam_grade)
    print("Ilu studentów dostało wyższą ocenę z egzaminu niż ich średnia ocen z laboratoriów?:",
          students_higher_exam_than_avg_lab)
    max_5_count_student_idx = np.argmax(np.sum(grades_data[:, :5] == 5, axis=1))
    num_5_grades_max_student = np.sum(grades_data[max_5_count_student_idx, :5] == 5)
    print("Liczba piątek, którą uzyskał student mający najwięcej 5 w całej grupie:", num_5_grades_max_student)


main()
