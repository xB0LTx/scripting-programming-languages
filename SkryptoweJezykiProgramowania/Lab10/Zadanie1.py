#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import matplotlib.pyplot as plt
import numpy as np
# stałe i zmienne globalne

# funkcje


def main() -> None:
    x = np.linspace(-np.pi, np.pi, 100)
    y_sin = np.sin(x)
    y_cos = 2 * np.cos(x)
    plt.plot(x, y_sin, label='sin(x)')
    plt.plot(x, y_cos, label='2cos(x)')
    plt.title('Wykresy funkcji sin(x) i 2cos(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
