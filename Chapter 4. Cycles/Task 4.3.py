# 4.3 Анализ бюджета
sum_per_month = int(input('Введите сумму выделенную на один месяц: '))
option_per_month = int(input('Введите количество статей расходов на месяц: '))
total = 0
for i in range(option_per_month):
    option = int(input(f'{i+1} статья расходов: '))
    total += option
result = sum_per_month - total
if result > 0:
    print(f'Вы сэкономили {result}$ за этот месяц')
else:
    print(f'Вы перерасходовали {result * (-1)}$ за этот месяц')
