# 11.2 Клас ShiftSupervisor

class Employee: # класс сотрудник
    def __init__(self, name, identifier):
        self.__name = name
        self.__identifier = identifier

    def set_name(self, name):
        self.__name = name

    def set_identifier(self, identifier):
        self.__identifier = identifier

    def get_name(self):
        return self.__name

    def get_identifier(self):
        return self.__identifier

    def __str__(self):
        return (f"Имя: {self.__name}\n"
                f"ID: {self.__identifier}\n")

class ShiftSupervisor(Employee): # класс начальник смены
    def __init__(self, name, identifier, salary, bonus):
        Employee.__init__(self, name, identifier)
        self.__salary = salary
        self.__bonus = bonus

    def set_salary(self, salary):
        self.__salary = salary

    def set_award(self, award):
        self.__bonus = award

    def get_salary(self):
        return self.__salary

    def get_award(self):
        return self.__bonus

    def __str__(self):
        return (f"{Employee.__str__(self)}"
                f"Оклад: {self.__salary}\n"
                f"Премия: {self.__bonus}\n")

def check_correct_input(question: str):
    questions = {1 : 'Введите имя рабочего: ',
                 2 : 'Введите ID рабочего: ',
                 3 : 'Введите оклад:',
                 4 : 'Введите премию: '}
    answer = input(question) # получаем ввод от пользователя
    if question == questions[1]: # проверяем ввод букв
        while not answer.isalpha(): # проверяем является ли ответ буквой, повторяем пока ответ не станет буквой
            answer = input(question)
        return answer
    else: # проверяем ввод цифр
        while not answer.isdigit(): # проверяем является ли ответ цифрой, повторяем пока не станет цифрой
            answer = input(question)
        return int(answer)

def main():
    name = check_correct_input('Введите имя рабочего: ')
    identifier = check_correct_input('Введите ID рабочего: ')
    salary = check_correct_input('Введите оклад: ')
    bonus = check_correct_input('Введите премию: ')
    boss = ShiftSupervisor(name, identifier, salary, bonus)
    print(boss)

if __name__ == "__main__":
    main()
