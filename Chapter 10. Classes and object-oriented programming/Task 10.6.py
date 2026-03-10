# 10.6 Расходы на лечение

class Patient:
    def __init__(self, first_name, last_name, patronymic, address, city, state, zip_code, phone, em_contact, em_phone):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__patronymic = patronymic
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__phone = phone
        self.__em_contact = em_contact
        self.__em_phone = em_phone

    # Методы мутаторы
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_patronymic(self, patronymic):
        self.__patronymic = patronymic

    def set_address(self, address):
        self.__address = address

    def set_city(self, city):
        self.__city = city

    def  set_state(self, state):
        self.__state = state

    def set_zip_code(self, zip_code):
        self.__zip_code = zip_code

    def set_phone(self, phone):
        self.__phone = phone

    def set_em_contact(self, em_contact):
        self.__em_contact = em_contact

    def set_em_phone(self, em_phone):
        self.__em_phone = em_phone

    def get_first_name(self):
        return self.__first_name
    # Методы получатели
    def get_last_name(self):
        return self.__last_name

    def get_patronymic(self):
        return self.__patronymic

    def get_address(self):
        return self.__address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip_code(self):
        return self.__zip_code

    def get_phone(self):
        return self.__phone

    def get_em_contact(self):
        return self.__em_contact

    def get_em_phone(self):
        return self.__em_phone

    def __str__(self):
        return (f"Имя, отчество и фамилия: {self.__first_name} {self.__last_name} {self.__patronymic}\n"
                f"Адрес, город, область и почтовый индекс: {self.__address} {self.__city} {self.__state} {self.__zip_code}\n"
                f"Телефонный номер: {self.__phone}\n"
                f"Имя и телефон контактного лица для экстренной связи: {self.__em_contact} {self.__em_phone}\n")

class Procedure:
    def __init__(self, name, date, doctor_name, price):
        self.__name = name
        self.__date = date
        self.__doctor_name = doctor_name
        self.__price = price
    # Методы мутаторы
    def set_name(self, name):
        self.__name = name

    def set_date(self, date):
        self.__date = date

    def set_doctor_name(self, doctor_name):
        self.__doctor_name = doctor_name

    def set_price(self, price):
        self.__price = price
    # Методы получатели
    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_doctor_name(self):
        return self.__doctor_name

    def get_price(self):
        return self.__price

    def __str__(self):
        return (f"Название процедуры: {self.__name}\n"
                f"Дата процедуры: {self.__date}\n"
                f"Имя врача, который выполнял процедуру: {self.__doctor_name}\n"
                f"Стоимость процедуры: {self.__price}\n")

def main():
    procedure1 = Procedure('врачебный осмотр', 'сегодняшняя', 'Ирвин', 250)
    procedure2 = Procedure('рентгенография', 'сегодняшняя', 'Джемисон', 500)
    procedure3 = Procedure('анализ крови', 'сегодняшняя', 'Смит', 200)
    pat = Patient('Джеймс', 'Эдвард', 'Джоунс', '123 Мэйн стрит',
                  'Биллингс', 'Монтана', '59000', '406-555-1212',
                  'Дженни Джоунс Jones', '406-555-1213')
    print(pat)
    print(procedure1)
    print(procedure2)
    print(procedure3)
    print(f"Общая стоимость всех процедур: {procedure1.get_price() + procedure2.get_price() + procedure3.get_price():,.2f}")

if __name__ == "__main__":
    main()
