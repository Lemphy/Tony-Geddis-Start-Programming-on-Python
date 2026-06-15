# 4.7 Мелкая монета для зарплаты
days = int(input('Количество дней для зарплаты: '))
total = 0
kopeek = 1
for day in range(days):
    total += kopeek
    print(f'{day+1} день - {kopeek} копеек')
    if day != days - 1:
        kopeek *= 2
print(f"Всего заработано {total/100} рублей.")
