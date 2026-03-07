# 10.3 Класс персональных данных Information

class Information:
    def __init__(self, name, age, address, phone_number):
        self.__name = name
        self.__age = age
        self.__address = address
        self.__phone_number = phone_number

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone_number(self):
        return self.__phone_number

    def __str__(self):
        return (f"Имя {self.__name}\n"
                f"Возраст {self.__age}\n"
                f"Адрес {self.__address}\n"
                f"Номер телефона {self.__phone_number}")

def main():
    users = list() # список пользователей
    for i in range(3): # собираем информацию о пользователях
        name = input("Введите имя: ")
        age = input("Введите возраст: ")
        address = input("Введите адрес: ")
        phone_number = input("Введите номер телефона: ")
        user = Information(name, age, address, phone_number)
        users.append(user)
    for user in users: # проходим список пользователей
        print(user) # передаем в класс метод на печать

if __name__ == "__main__":
    main()
