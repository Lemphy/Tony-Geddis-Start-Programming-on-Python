# 5.6 Калории за счет жиров и углеводов
FATS = 9
CARBOHYDRATES = 4

def calc_fats(arg):
    return arg * FATS

def calc_carbohydrates(arg):
    return arg * CARBOHYDRATES

def main():
    fats = int(input('Сколько грамм жиров вы употребили за сегодня? '))
    carbohydrates = int(input('Сколько грамм углеводов вы употребили сегодня? '))
    print(f"Калории от жиров: {calc_fats(fats):,.2f}\n"
          f"Калории от углеводов: {calc_carbohydrates(carbohydrates):,.2f}")

if __name__ == '__main__':
    main()
