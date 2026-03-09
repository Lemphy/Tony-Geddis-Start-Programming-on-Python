# 10.4 Класс Employee

class Employee:
    def __init__(self, name, identifier, department, post):
        self.__name = name
        self.__identifier = identifier
        self.__department = department
        self.__post = post

    def __str__(self):
        return (f"Имя: {self.__name}\n"
                f"ID: {self.__identifier}\n"
                f"Отдел: {self.__department}\n"
                f"Должность: {self.__post}\n")

def make_list(): # заполняем список экземплярами
    temp = list()
    for i in range(3):
        name = input("Имя: ")
        identifier = input("ID: ")
        department = input('Отдел: ')
        post = input('Должность: ')
        person = Employee(name, identifier, department, post)
        temp.append(person)
    return temp

def show_list(temp): # показать информацию о сотрудниках
    for x in temp: # проходим по каждому объекту
        print(x) # печатаем состояние текущего объекта

def main():
    peoples = make_list()
    print("Информация о сотрудниках")
    show_list(peoples)

if __name__ == "__main__":
    main()
