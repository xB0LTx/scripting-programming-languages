#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import re
# stałe i zmienne globalne

# funkcje


def fix_capitalization(match):
    word = match.group(0)
    if len(word) > 2:
        return word.capitalize()
    else:
        user_input = input(f"Czy chcesz naprawić słowo: '{word}'? (t/n): ")
        if user_input.lower().strip() == 't':
            return word.capitalize()
        else:
            return word


def correct_capitalization(text):
    pattern = re.compile(r'\b([A-Z]{2}[a-z]*|[a-z]+[A-Z]+[a-z]*|[A-Z][a-z]*[A-Z]+[a-z]*)\b')
    corrected_text = pattern.sub(fix_capitalization, text)
    return corrected_text


def main() -> None:
    text = \
        "BYdgoszcz to piękne miasto. POlska ma niezwykłą historię. PoliTEchnika Bydgoska jest super. IT jest ciekawe."
    corrected_text = correct_capitalization(text)
    print("Pierwotny tekst:", text)
    print("Poprawiony tekst:", corrected_text)


main()
