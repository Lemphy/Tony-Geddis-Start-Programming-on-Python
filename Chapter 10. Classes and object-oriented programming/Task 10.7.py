# 10.7 Система управления персоналом

import pickle
FIND = 1
ADD = 2
CHANGE = 3
REMOVE = 4
LOOK_UP = 5
QUIT = 6
FILENAME = 'employee.dat'

class Employee:
    def __init__(self, name, identifier, department, post):
        self.__name = name
        self.__identifier = identifier
        self.__department = department
        self.__post = post
    # Методы мутаторы
    def set_name(self, name):
        self.__name = name

    def set_identifier(self, identifier):
        self.__identifier = identifier

    def set_department(self, department):
        self.__department = department

    def set_post(self, post):
        self.__post = post
    # Методы получатели
    def get_name(self):
        return self.__name

    def get_identifier(self):
        return self.__identifier

    def get_department(self):
        return self.__department

    def get_post(self):
        return self.__post

    def __str__(self):
        return (f"Имя: {self.__name}\n"
                f"ID: {self.__identifier}\n"
                f"Отдел: {self.__department}\n"
                f"Должность: {self.__post}\n")

def show_menu(): # показать меню
    print(f"Выберите нужный вариант из меню\n"
          f"1. Найти сотрудника в словаре\n"
          f"2. Добавить нового сотрудника в словарь\n"
          f"3. Изменить имя, отдел, и должность существующего сотрудника в словаре\n"
          f"4. Удалить сотрудника из словаря\n"
          f"5. Показать содержимое словаря\n"
          f"6. Выйти из программы")

def get_correct_user_answer(mode): # получить корректный ответ пользователя
    while True: # функция имеет 3 режима работы
        if mode == 'CHECK_THE_ITEM_MENU_SELECTION': # проверить выбор пункта меню
            try:
                user_answer = int(input("Ответ: "))
                while user_answer < FIND or user_answer > QUIT:
                    print(f"Число должно быть в диапазоне от {FIND}до {QUIT}")
                    user_answer = int(input("Ответ: "))
            except ValueError:
                print("Ответ должен быть цифрой.")
            else:
                return user_answer
        elif mode == 'CHECK_THE_CORRECT_ID': # проверить правильность ввода ID сотрудника
            key = input("Введите идентификационный номер сотрудника: ")
            while not key.isdigit():  # если ответ содержит что-либо кроме цифр
                print("Номер сотрудника должен состоять только из цифр.")
                key = input("Введите идентификационный номер сотрудника: ")
            return key
        elif mode == 'CHECK_THE_CORRECT_FIELD_TO_OBJECT': # проверить правильность ввода новых данных сотрудника
            name = input("Введите имя сотрудника: ")
            department = input("Введите отдел сотрудника: ")
            post = input("Введите должность сотрудника: ")
            return name, department, post

def open_file(): # получить данные из файла
    try:
        infile = open(FILENAME, 'rb')
    except FileNotFoundError: # если файла нету
        mydict = dict() # создаем пустой словарь и возвращаем на него ссылку
    else:
        mydict = pickle.load(infile)
        infile.close()
    return mydict

def save_and_exit(dct): # сохранить и выйти
    if dct: # если в словаре есть элементы, сохраняем их в файл
        outfile = open(FILENAME,'wb')
        pickle.dump(dct,outfile)
        outfile.close()
        print("Программа успешно закрыта.\n")
    else: # если элементов нет, то и сохранять в файл нечего
        print("Программа успешно закрыта.\n")

def find_employee(dct): # найти сотрудника в словаре
    key = get_correct_user_answer('CHECK_THE_CORRECT_ID')
    value = dct.get(key, "Сотрудник с таким идентификационным номером не обнаружен.\n")
    print(value)

def add_employee(dct): # добавь сотрудника в словарь
    key = get_correct_user_answer('CHECK_THE_CORRECT_ID')
    if key not in dct: # если ID нет в словаре
        name, department, post = get_correct_user_answer('CHECK_THE_CORRECT_FIELD_TO_OBJECT')
        user = Employee(name, key, department, post)
        dct[key] = user
        print("Успешно добавлено в словарь.\n")
    else: # если ID уже есть в словаре
        print("Сотрудник с таким идентификационным номером уже находится в словаре.\n")

def change_employee(dct): # изменить имя, отдел и должность существующего сотрудника в словаре
    key = get_correct_user_answer('CHECK_THE_CORRECT_ID')
    if key in dct: # если ID есть в словаре
        name, department, post = get_correct_user_answer('CHECK_THE_CORRECT_FIELD_TO_OBJECT')
        user = dct[key] # получаем значение по ключу в виде объекта и присваиваем ссылку на этот объект переменной user
        user.set_name(name) # применяем методы модификаторы к объекту
        user.set_department(department)
        user.set_post(post)
        print("Успешно изменено.\n")
    else:
        print("Сотрудник с таким идентификационным номером не обнаружен.\n")

def look_up_employee(dct): # показать всех сотрудников
    if dct: # если в словаре есть элементы
        for key in dct: # проходим по ключам словаря
            print(dct[key]) # печатаем что содержит объект по данному ключу
    else:
        print("Словарь пуст.\n")

def remove_employee(dct): # удалить сотрудника по ID из словаря
    key = get_correct_user_answer('CHECK_THE_CORRECT_ID')
    if key in dct:
        del dct[key]
        print(f"Сотрудник с ID: {key} успешно удален.\n")
    else:
        print("Сотрудник с таким идентификационным номером не обнаружен.\n")

def main():
    user_answer = 0
    dictionary = open_file()
    while user_answer != QUIT:
        show_menu()
        user_answer = get_correct_user_answer('CHECK_THE_ITEM_MENU_SELECTION')
        if user_answer == FIND:
            find_employee(dictionary)
        elif user_answer == ADD:
            add_employee(dictionary)
        elif user_answer == CHANGE:
            change_employee(dictionary)
        elif user_answer == REMOVE:
            remove_employee(dictionary)
        elif user_answer == LOOK_UP:
            look_up_employee(dictionary)
    save_and_exit(dictionary)

if __name__ == "__main__":
    main()
