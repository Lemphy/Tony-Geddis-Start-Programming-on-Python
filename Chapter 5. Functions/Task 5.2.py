# 5.2 Модернизация программы расчета налога с продаж

FEDERAL_TAX = 0.05
REGIONAL_TAX = 0.02

def calc_federal_tax(arg1):
    return arg1 * FEDERAL_TAX

def calc_regional_tax(arg1):
    return arg1 * REGIONAL_TAX

def main():
    price = int(input('Введите сумму покупки товара: '))
    print(f"Стоимость товара: {price:,.2f}$\n"
          f"Федеральных налог, включенный в стоимость: {calc_federal_tax(price):,.2f}$\n"
          f"Региональный налог, включенный в стоимость: {calc_regional_tax(price):,.2f}$")

if __name__ == '__main__':
    main()
