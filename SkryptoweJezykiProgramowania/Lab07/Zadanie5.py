#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import re
# stałe i zmienne globalne

# funkcje


def polish_phone_numbers(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.readlines()
    pattern = r'(\+48|0048)'
    polish_numbers_list = []
    for number in text:
        if re.match(pattern, number):
            polish_numbers_list.append(number)
    print("Polskie numery telefoniczne znalezione w pliku:")
    for number in polish_numbers_list:
        print(number)


def main() ->None:
    polish_phone_numbers("numery.txt")


main()
