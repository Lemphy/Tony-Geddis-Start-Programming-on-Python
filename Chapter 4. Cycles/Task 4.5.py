# 4.5 Средняя толщина слоя дождевых осадков
MONTH_PER_YEAR = 12
years = int(input("Введите количество лет для анализа: "))
total = 0
for i in range(years):
    for x in range(MONTH_PER_YEAR):
        value = int(input(f"Количество дождевых осадков за {x+1}-ый месяц {i+1}-го года: "))
        total += value
total_months = years * MONTH_PER_YEAR
print(f'Общее количество дождевых осадков: {total}\n'
      f'Средняя толщина слоя дождевых осадков в месяц в течении всего периода: {total/total_months}')
