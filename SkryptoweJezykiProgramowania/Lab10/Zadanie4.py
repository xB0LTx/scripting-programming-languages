#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import matplotlib.pyplot as plt
import numpy as np
# stałe i zmienne globalne

# funkcje


def main() -> None:
    x = np.linspace(0, 9, 10)
    y1 = np.random.randint(0, 100, size=10)
    y2 = np.random.randint(0, 100, size=10)
    y3 = np.random.randint(0, 100, size=10)
    plt.plot(x, y1, 'gD-', label='Zielone diamenty')
    plt.plot(x, y2, 'y*--', label='Żółte gwiazdki')
    plt.plot(x, y3, 'mp-.', label='Fioletowe pięciokąty')
    plt.xlabel('Oś X')
    plt.ylabel('Oś Y')
    plt.title('Wykres liniowy z różnymi formatowaniami linii')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
