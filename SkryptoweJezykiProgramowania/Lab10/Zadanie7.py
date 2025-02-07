#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import matplotlib.pyplot as plt
import numpy as np
# stałe i zmienne globalne

# funkcje


def main() -> None:
    x = np.linspace(0, 2 * np.pi)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.tan(x)
    y4 = np.arctan(x)
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 2, 1)
    plt.plot(x, y1, label='sin(x)')
    plt.title('sin(x)')
    plt.legend()
    plt.subplot(2, 2, 2)
    plt.plot(x, y2, label='cos(x)', color='orange')
    plt.title('cos(x)')
    plt.legend()
    plt.subplot(2, 2, 3)
    plt.plot(x, y3, label='tan(x)', color='green')
    plt.title('tan(x)')
    plt.ylim(-5, 5)  # Ustawienie ograniczenia osi Y dla lepszej widoczności
    plt.legend()
    plt.subplot(2, 2, 4)
    plt.plot(x, y4, label='arctan(x)', color='red')
    plt.title('arctan(x)')
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
