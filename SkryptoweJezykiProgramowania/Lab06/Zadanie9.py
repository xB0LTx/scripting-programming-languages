#!C:\Users\koksu\AppData\Local\Programs\Python\Python310

# importy
import typing
import pickle
# stałe i zmienne globalne

# funkcje


class Person:
    def __init__(self, name: str, age: int, hobbies: list) -> None:
        self.name = name
        self.age = age
        self.hobbies = hobbies

    def export_to_file(self, filename: str) -> None:
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
            print(f"Instance of {self.__class__.__name__} has been exported to '{filename}'.")
        except Exception as e:
            print(f"Error exporting instance: {e}")

    @classmethod
    def import_from_file(cls, filename: str) -> any:
        try:
            with open(filename, "rb") as file:
                instance = pickle.load(file)
            if isinstance(instance, cls):
                print(f"Instance of {cls.__name__} has been imported from '{filename}'.")
                return instance
            else:
                print(f"Error: The imported object is not an instance of {cls.__name__}.")
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except Exception as e:
            print(f"Error importing instance: {e}")


def main() -> None:
    person = Person("John", 30, ["Reading", "Hiking"])
    person.export_to_file("person_data.pkl")
    imported_person = Person.import_from_file("person_data.pkl")
    if imported_person:
        print(f"Imported Person: Name - {imported_person.name}, Age - {imported_person.age}, "
              f"Hobbies - {imported_person.hobbies}")


main()
