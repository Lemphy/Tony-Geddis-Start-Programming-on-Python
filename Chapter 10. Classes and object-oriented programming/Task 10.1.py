# 10.1 Класс Pet

class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name # кличка животного
        self.__animal_type = animal_type # тип животного
        self.__age = age # возраст животного

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

def main():
    animal_name = input("Введите кличку животного: ")
    animal_type = input("Введите тип животного: ")
    animal_age = input("Введите возраст животного: ")
    animal = Pet(animal_name, animal_type, animal_age)
    print(f"Имя: {animal.get_name()}\n"
          f"Тип: {animal.get_animal_type()}\n"
          f"Возраст: {animal.get_age()}")

if __name__ == "__main__":
    main()
