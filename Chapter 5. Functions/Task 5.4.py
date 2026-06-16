# 5.4 Расходы на автомобиль

def calc_monthly_price(arg1,arg2,arg3,arg4,arg5,arg6):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6

def calc_yearly_price(arg1):
    return arg1 * 12

def main():
    credit = int(input('Расходы на кредит: '))
    insurance = int(input('Расходы на страховку: '))
    petrol = int(input('Расходы на бензин: '))
    machine_oil = int(input('Расходы на машинное масло: '))
    tire = int(input('Расходы на покрышки: '))
    repair = int(input('Расходы на техобслуживание: '))
    monthly_price = calc_monthly_price(credit, insurance, petrol, machine_oil, tire, repair)
    yearly_price = calc_yearly_price(monthly_price)
    print(f'Цена обслуживания за месяц: {monthly_price:,.2f}$\n'
          f'Цена обслуживания за год: {yearly_price:,.2f}$')

if __name__ == '__main__':
    main()
