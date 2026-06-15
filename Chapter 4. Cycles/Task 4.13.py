# 4.13 Популяция
value = int(input('Стартовое количество: '))
average = int(input('Среднесуточное увеличение %: ')) / 100
days = int(input('Количество дней для размножения: '))
print('День\t\tПопуляция')
print('-' * 21)
for day in range(1, days + 1):
    print(f'{day}\t\t\t{value: ,.3f}')
    if day != days:
        value *= average + 1
