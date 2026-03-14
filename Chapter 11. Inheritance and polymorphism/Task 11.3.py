# 11.3 Классы Person и Customer

class Person:
    def __init__(self, name, email, phone):
        self.__name = name
        self.__email = email
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

class Customer(Person):
    def __init__(self, name, email, phone, customer_id, mailing):
        Person.__init__(self, name, email, phone)
        self.__customer_id = customer_id
        self.__mailing = mailing

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_mailing(self, mailing):
        self.__mailing = mailing

    def get_customer_id(self):
        return self.__customer_id

    def get_mailing(self):
        return self.__mailing

def check_mailing():# проверка хочет ли клиент получать рассылку
    arg = input("Рассылка (да/нет): ")
    while True:
        if arg == 'да':
            return True
        elif arg == 'нет':
            return False
        else:
            arg = input("Рассылка (да/нет): ")

def main():
    name = input("Введите имя клиента: ")
    email = input("Введите эмейл клиента: ")
    phone = input("Введите номер телефона клиента: ")
    customer_id = input("Введите ID клиента: ")
    mailing = check_mailing()
    customer1 = Customer(name = name, email = email, phone = phone, customer_id = customer_id, mailing = mailing)
    print(f"Имя: {customer1.get_name()}\n"
          f"Эмейл: {customer1.get_email()}\n"
          f"Номер телефона: {customer1.get_phone()}\n"
          f"ID: {customer1.get_customer_id()}\n"
          f"Рассылка: {customer1.get_mailing()}\n")

if __name__ == "__main__":
    main()
