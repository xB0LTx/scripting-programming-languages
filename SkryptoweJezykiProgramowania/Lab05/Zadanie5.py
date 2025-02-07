#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import random
# stałe i zmienne globalne

# funkcje


def main() -> None:
    games_played = 0
    games_won = 0
    while True:
        user_choice = input("Wybierz: papier (P), kamień (R), nożyce (S), lub 'X' aby zakończyć: ").upper()
        if user_choice == 'X':
            break
        if user_choice not in ('P', 'R', 'S'):
            print("Nieprawidłowy wybór. Wprowadź 'P', 'R', 'S' lub 'X'.")
            continue
        computer_choice = random.choice(['P', 'R', 'S'])
        print(f"Twój wybór: {user_choice}")
        print(f"Wybór komputera: {computer_choice}")
        if user_choice == computer_choice:
            print("Remis!")
        elif (user_choice == 'P' and computer_choice == 'R') or (user_choice == 'R' and computer_choice == 'S') or (user_choice == 'S' and computer_choice == 'P'):
            print("Wygrałeś!")
            games_won += 1
        else:
            print("Komputer wygrał.")
        games_played += 1
    print(f"Liczba rozegranych gier: {games_played}")
    print(f"Liczba wygranych gier: {games_won}")


main()
