#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import matplotlib.pyplot as plt
# stałe i zmienne globalne

# funkcje


def main() -> None:
    fig, ax = plt.subplots()
    fruits = ['apple', 'blueberry', 'cherry', 'orange', 'pineapple']
    counts = [40, 100, 30, 55, 70]
    bar_labels = ['red', 'blue', '_red', 'orange', 'green']
    bar_colors = ['red', 'blue', 'red', 'orange', 'green']
    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
    ax.set_ylabel('Number of Fruits')
    ax.set_title('Fruit Counts')
    ax.legend(title='Bar Colors')
    plt.show()


if __name__ == "__main__":
    main()
