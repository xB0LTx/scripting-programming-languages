#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing

# stałe i zmienne globalne

# funkcje


def zadanie10() -> None:
    rndm_dict = {
        "fruit": "strawberry",
        "vegetable": "carrot",
        "candy": "fudge",
        "beverage": "beer"
    }
    print("Zadanie 10\nSłownik początkowy:\n", rndm_dict)
    rndm_dict["kitchenware"] = "spoon"
    print("\na):\n", rndm_dict)
    rndm_dict["fruit"] = "mango"
    print("\nb):\n", rndm_dict)
    pop = rndm_dict.pop("candy")
    popitem = rndm_dict.popitem()
    print("\nc) metoda pop: ", pop, ", metoda popitem", popitem)
    rndm_dict_2 = {
        1: "strawberry",
        "vegetable": "carrot",
        3: "fudge",
        "beverage": "beer"
    }
    rndm_dict_3 = {
        "fruit": "strawberry",
        "vegetable": 2,
        "candy": "fudge",
        "beverage": 4
    }
    print("\nd) Możliwe jest użycie w jednym słowniku kluczy o dwóch różnych typach."
          "Możliwe jest również użycie w jednym słowniku wartości o różnych typach.")


def main() -> None:
    zadanie10()


main()
