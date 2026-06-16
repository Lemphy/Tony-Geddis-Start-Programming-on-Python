# 5.3 Какова стоимость страховки?
TAX = 80

def calc_tax(arg1):
    return arg1 * (TAX/100)

def main():
    price_of_house = int(input('Введите стоимость строения: '))
    print(f"Минимальная страховка: {calc_tax(price_of_house):,.2f}%")

if __name__ == '__main__':
    main()
