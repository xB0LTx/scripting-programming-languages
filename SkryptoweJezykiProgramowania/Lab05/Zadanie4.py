#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import random
# stałe i zmienne globalne

# funkcje


def flip_coin() -> int:
    result = random.randint(0, 1)
    return result


def main() -> None:
    games_played = 0
    games_won = 0

    while True:
        user_choice = input("Obstaw orła (O) lub reszkę (R), lub wprowadź 'X' aby zakończyć: ").upper()

        if user_choice == 'X':
            break  # Zakończ grę

        if user_choice not in ('O', 'R'):
            print("Nieprawidłowy wybór. Wprowadź 'O', 'R' lub 'X'.")
            continue

        # Rzut monetą
        coin_result = flip_coin()
        if (coin_result == 0 and user_choice == 'O') or (coin_result == 1 and user_choice == 'R'):
            print("Wygrałeś!")
            games_won += 1
        else:
            print("Przegrałeś.")

        games_played += 1

    print(f"Liczba rozegranych gier: {games_played}")
    print(f"Liczba wygranych gier: {games_won}")


main()
