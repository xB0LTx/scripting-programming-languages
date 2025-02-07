#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import matplotlib.pyplot as plt
# stałe i zmienne globalne

# funkcje


def main() -> None:
    labels = 'Frogs', 'Cats', 'Dogs', 'Birds'
    sizes = [25, 30, 45, 20]
    explode = (0, 0.1, 0, 0.1)  # Dodane przesunięcia dla sektorów
    shadow = True  # Dodany cień
    start_angle = 90  # Zmieniony kąt początkowy
    fig1, ax1 = plt.subplots()
    ax1.pie(
        sizes,
        explode=explode,
        labels=labels,
        autopct='%1.1f%%',
        shadow=shadow,
        startangle=start_angle
    )
    ax1.legend(labels, loc="best")
    plt.show()


if __name__ == "__main__":
    main()
