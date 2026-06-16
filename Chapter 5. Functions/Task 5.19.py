# 5.19 Будущая стоимость

def future_total(p, i, t):
    return p * (1 + (i/100)) ** t

def main():
    p = int(input('Введите текущую сумму на счете: '))
    i = int(input('Ежемесячная процентная ставка: '))
    t = int(input('Количество месяцев: '))
    print(f'Будущая сумма на счете: {future_total(p, i, t)}')

if __name__ == '__main__':
    main()
