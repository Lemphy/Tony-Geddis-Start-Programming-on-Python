# 10.5 Класс RetailItem

class RetailItem:
    def __init__(self, description, amount, price):
        self.__description = description
        self.__amount = amount
        self.__price = price

    def __str__(self):
        return (f"Описание: {self.__description}\n"
                f"Количество на складе: {self.__amount}\n"
                f"Цена: {self.__price}\n")

def main():
    product1 = RetailItem('Пиджак', 12, 59.95)
    product2 = RetailItem('Дизайнерские джинсы', 40, 34.95)
    product3 = RetailItem('Рубашка', 20, 24.95)
    print('Товар 1', product1, sep = '\n')
    print('Товар 2', product2, sep = '\n')
    print('Товар 3', product3, sep = '\n')

if __name__ == "__main__":
    main()
