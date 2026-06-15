# 4.8 Сумма чисел
total = 0
number = 0
while number >= 0:
    number = int(input('Введите положительное число (отрицательное для выхода): '))
    total += number
print(f'Сумма чисел: {total}')
