# 5.9 Месячный налог с продаж
MYNICIPAL_TAX = 2.5
FEDERAL_TAX = 5

def calc_tax(value):
    return (MYNICIPAL_TAX/100) * value, (FEDERAL_TAX/100) * value

def main():
    total_sales = int(input('Введите общий объем продаж за месяц: '))
    mynicipal, federal = calc_tax(total_sales)
    print(f"Муниципальный налог: {mynicipal:,.2f}$\n"
          f"Федеральный налог: {federal:,.2f}$\n"
          f"Общая сумма налога: {mynicipal + federal:,.2f}$")

if __name__ == '__main__':
    main()
