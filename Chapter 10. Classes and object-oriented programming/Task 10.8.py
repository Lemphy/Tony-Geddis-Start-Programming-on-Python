# 10.8 класс CashRegister

class RetailItem:
    def __init__(self, description, amount, price):
        self.__description = description
        self.__amount = amount
        self.__price = price

    def set_amount(self, amount):
        self.__amount = amount

    def get_description(self):
        return self.__description

    def get_amount(self):
        return self.__amount

    def get_price(self):
        return self.__price

    def __str__(self):
        return (f"Описание: {self.__description}\n"
                f"Количество на складе: {self.__amount}\n"
                f"Цена: {self.__price}")

class CashRegister:
    def __init__(self):
        self.__objects = []

    def purchase_item(self, item): # приобрести товар
        self.__objects.append(item)
        print("Товар был добавлен в чек.")

    def get_total(self): # получить сумму покупки товаров
        total = 0
        for obj in self.__objects:
            total += obj.get_price()
        return total

    def show_items(self): # показать список купленных товаров
        for obj in self.__objects:
            print(obj)

    def clear(self): # очистить список товаров
        self.__objects = list()

def create_dict(): # создаем словарь содержащий объекты в виде предметов на полках магазина
    blazer = RetailItem('Пиджак', 12, 59.95)
    designer_jeans = RetailItem('Дизайнерские джинсы', 40, 34.95)
    shirt = RetailItem('Рубашка', 20, 24.95)
    socks = RetailItem('Носки', 10, 13.95)
    t_shirt = RetailItem('Футболка', 10, 20.50)
    shorts = RetailItem('Шорты', 15, 18.95)
    sale_items = {1: blazer, 2: designer_jeans, 3: shirt, 4: socks, 5: t_shirt, 6: shorts}
    return sale_items

def show_items(dct): # показывает текущее состояние вещей на полках магазина
    for k,v in dct.items():
        print('*' * 30)
        print(f"Товар №{k}\n{v}")

def get_need_item(dct): # проверка правильности ввода номера товара
    while True:
        try:
            answer = int(input("Выберите из списка желаемый товар: "))
            while answer < 1 or answer > len(dct):
                print("Введите допустимый номер товара.")
                answer = int(input("Выберите из списка желаемый товар: "))
        except ValueError:
            print("Ответ должен быть числом")
        else:
            return answer

def main():
    mydict = create_dict() # создаем словарь с товарами
    answer = 'н'
    register = CashRegister()
    while answer.lower() == 'н': # инициализируем цикл для наполнения покупок
        show_items(mydict) # показываем текущее состояние предметов на полках магазина
        item = mydict[get_need_item(mydict)] # получаем ссылку на объект введя его номер как ключ
        amount = item.get_amount() # присваиваем переменной количество оставшихся товаров на полке
        if amount != 0: # если товар еще остался на полках
            register.purchase_item(item)
            item.set_amount(amount - 1) # забираем 1 товар
        else:
            print("Данный товар закончился.")
        answer = input("Готовы оформить покупку? (д/н): ")
    print(f"Список покупок:")
    register.show_items()
    print(f"Общая сумма покупок\n{register.get_total()}")

if __name__ == "__main__":
    main()
