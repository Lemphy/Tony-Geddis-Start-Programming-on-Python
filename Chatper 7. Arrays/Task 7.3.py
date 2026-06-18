# 7.3 Статистика дождевых осадков

def main():
    month_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль',
                  'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    month_rain = []
    # Ввод количества осадков
    for month in range(len(month_list)):
        temp = int(input(f'Количество осадков за {month_list[month]}: '))
        month_rain.append(temp)

    # Суммарное количество осадков за год
    total = 0
    for i in month_rain:
        total += i

    average = total / len(month_list) # среднее за все время
    min_month_value = min(month_rain) # минимальное количество
    min_month = month_list[month_rain.index(min_month_value)] # месяц с минимальным количеством
    max_month_value = max(month_rain) # максимальное количество
    max_month = month_list[month_rain.index(max_month_value)] # месяц с максимальным количеством
    print(f'Суммарное количество дождевых осадков за год: {total:,.1f}\n'
          f'Среднее ежемесячное количество дождевых осадков: {average:,.1f}\n'
          f'Месяц с минимальным количеством дождевых осадков: {min_month} - {min_month_value}\n'
          f'Месяц с максимальным количеством дождевых осадков: {max_month} - {max_month_value}\n')

if __name__ == '__main__':
    main()
