# 4.1 Сборщик ошибок

DAYS = 5
total = 0
for i in range(1, DAYS + 1):
    print(f'Введите количество ошибок за {i}-день: ', end = '')
    mistakes = int(input())
    total += mistakes # добавляем в аккумулятор значение
print(f'Общее количество ошибок за {DAYS} дней: {total}')
