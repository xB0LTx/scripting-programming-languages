#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import matplotlib.pyplot as plt
import numpy as np
# stałe i zmienne globalne

# funkcje


def main() -> None:
    data = np.genfromtxt('../Lab09/oceny.csv', delimiter='\t', skip_header=1)
    lab_grades = data[:, :-1]
    flat_lab_grades = lab_grades.flatten()
    grades, grades_counts = np.unique(flat_lab_grades, return_counts=True)
    plt.figure(figsize=(8, 8))
    plt.pie(grades_counts, labels=grades, autopct='%1.1f%%', startangle=90,
            colors=['red', 'orange', 'yellow', 'green', 'blue', 'purple'])
    plt.title('Liczba Poszczególnych Oceny z Laboratoriów')
    plt.legend(grades, title='Oceny', loc="best")
    plt.savefig('Ilość ocen.png')
    plt.show()


if __name__ == "__main__":
    main()

