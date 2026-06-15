# 4.11 Потеря массы
WEIGHT_LOSS_EVERY_MONTH = 1.5
weight = int(input('Введите вашу массу в кг: '))
months = int(input('Количество месяцев для похудения: '))
print('Вес\t\tМесяц')
print('-' * 13)
for month in range(1, months + 1):
    weight -= WEIGHT_LOSS_EVERY_MONTH
    print(f'{weight}\t\t{month}')
