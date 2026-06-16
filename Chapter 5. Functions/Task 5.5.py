# 5.5 Налог на недвижимое имущество
TAX_ESTIMATED_VALUE = 60
PROPERTY_TAX = 72

def calc_estimated_value(arg1): # оценочная стоимость
    return arg1 * (TAX_ESTIMATED_VALUE/100)

def calc_property_tax(arg1): # налог на имущество
    return (arg1 / 100) * (72/100)

def main():
    price = int(input('Введите фактическую стоимость недвижимого имущества: '))
    estimated_value = calc_estimated_value(price)
    print(f"Оценочная стоимость имущества: {estimated_value:,.2f}$\n"
          f"Налог на имущество: {calc_property_tax(estimated_value):,.2f}$")

if __name__ == '__main__':
    main()
