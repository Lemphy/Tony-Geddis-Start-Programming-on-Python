# 4.12 Вычисление факториала числа
number = int(input('Введите число для вычисления его факториала: '))
total = 1
print(f'{number}! = ', end = '')
for i in range(1, number + 1):
    total *= i
    if i != number:
        print(f'{i} * ', end = '')
    else:
        print(f'{i} = {total}')
