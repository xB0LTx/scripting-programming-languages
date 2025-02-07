#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing

# stałe i zmienne globalne

# funkcje


def main() -> None:
    try:
        # Dla każdego z trzech trybów: 'a', 'w', 'x'
        for mode in ['a', 'w', 'x']:
            file_name = f"test_file_{mode}.txt"
            content = f"Hello, this is a test file in '{mode}' mode."

            # Próba otwarcia istniejącego pliku
            with open(file_name, mode) as file:
                file.write(content)
                print(f"File '{file_name}' opened in '{mode}' mode and content written successfully.")

            # Próba otwarcia nieistniejącego pliku
            non_existent_file_name = f"non_existent_file_{mode}.txt"
            with open(non_existent_file_name, mode) as file:
                file.write(content)
                print(f"File '{non_existent_file_name}' opened in '{mode}' mode and content written successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")


main()
