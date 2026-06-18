# 7.1 Общий объем продаж
WEEK = 7

def main():
    paid_list = []
    for i in range(WEEK):
        sales_today = int(input(f'Сумма продаж за {i + 1} день: '))
        paid_list.append(sales_today)
    total = 0
    for value in paid_list:
        total += value
    print('Общий объем продаж за неделю:', total)

if __name__ == '__main__':
    main()
