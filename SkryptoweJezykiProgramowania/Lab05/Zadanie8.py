#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing

# stałe i zmienne globalne

# funkcje


def xor_cipher(text: str, key: str) -> str:
    encrypted_text = ""
    for i in range(len(text)):
        char = text[i]
        key_char = key[i]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        encrypted_text += encrypted_char
    return encrypted_text


def main() -> None:
    plaintext = input("Podaj tekst:")
    keyword = input("Podaj słowo szyfrowe:")
    xor_text = xor_cipher(plaintext, keyword)
    xor_text2 = xor_cipher(xor_text, keyword)
    print("Tekst po operacji xor:", xor_text, xor_text2)


main()
