# 11.1 Классы Employee и ProductionWorker

class Employee:
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

class ProductionWorker(Employee):
    def __init__(self, name, identifier, number, price):
        Employee.__init__(self,name,identifier)
        self.__number = number
        self.__price = price

    def set_number(self, number):
        self.__number = number

    def set_price(self,price):
        self.__price = price

    def get_number(self):
        return self.__number

    def get_price(self):
        return self.__price

    def __str__(self):
        return (f"{Employee.__str__(self)}"
                f"Смена: {self.__number}\n"
                f"Ставка почасовой оплаты: {self.__price}\n")

def check_correct_input(question):
    questions = {1 : 'Введите имя рабочего: ',
                 2 : 'Введите ID рабочего: ',
                 3 : 'Введите номер смены: дневная/ночная (1/2):',
                 4 : 'Введите почасовую ставку оплаты труда: '}
    answer = input(question) # получаем ввод от пользователя
    if question == questions[1]: # проверяем ввод букв
        while not answer.isalpha(): # проверяем является ли ответ буквой, повторяем пока ответ не станет буквой
            answer = input(question)
        return answer

    elif question == questions[2] or question == questions[3] or question == questions[4]: # проверяем ввод чисел
        if question == questions[3]: # если вопрос про смену 1/2
            while answer != '1' and answer != '2':
                answer = input(question)
            if answer == '1':
                return 'дневная'
            else:
                return 'ночная'

        else: # если вопросы не требующие диапазона чисел
            while not answer.isdigit(): # проверяем является ли ответ цифрой, повторяем пока не станет цифрой
                answer = input(question)
            return int(answer)
    else:
        return None

def main():
    name = check_correct_input('Введите имя рабочего: ')
    identifier = check_correct_input('Введите ID рабочего: ')
    number = check_correct_input('Введите номер смены: дневная/ночная (1/2):')
    price = check_correct_input('Введите почасовую ставку оплаты труда: ')
    worker = ProductionWorker(name, identifier, number, price)
    print(worker)

if __name__ == "__main__":
    main()
