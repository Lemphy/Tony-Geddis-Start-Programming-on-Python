# 4.6 Таблица соответствия между градусами Цельсия и градусами Фаренгейта
print('Цельсия\t\tФаренгейта')
print('-' * 22)
for celsium in range(21):
    farengeit = (9/5)*celsium+32
    print(f'{celsium:>7.1f}\t\t{farengeit:>10.1f}')
