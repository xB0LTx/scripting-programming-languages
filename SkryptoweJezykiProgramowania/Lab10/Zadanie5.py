#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import matplotlib.pyplot as plt
import numpy as np
# stałe i zmienne globalne

# funkcje


def main() -> None:
    data = np.random.randint(0, 10, 100)
    unique_values, counts = np.unique(data, return_counts=True)
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.bar(unique_values, counts, color='blue')
    plt.title('Wykres Słupkowy')
    plt.xlabel('Wartość')
    plt.ylabel('Liczba Powtórzeń')
    plt.subplot(1, 2, 2)
    plt.hist(data, bins=np.arange(11) - 0.5, color='green', edgecolor='black')
    plt.title('Histogram')
    plt.xlabel('Wartość')
    plt.ylabel('Liczba Powtórzeń')
    plt.show()


if __name__ == "__main__":
    main()
