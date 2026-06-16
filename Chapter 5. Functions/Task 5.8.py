# 5.8 Оценщик малярных работ
SQUARE_METR = 10 # количество квадратных метров
ONE_COLOR = 5 # емкость одной банки краски в литрах
COLOR = ONE_COLOR / SQUARE_METR # 5 литров краски на 10 квадратных метров, узнаем за 1 квадратный метр количество краски
TIME = 8 / SQUARE_METR # 8 часов работы на 10 квадратных метров, узнаем за 1 квадратный метр количество времени в часах
PRICE_OF_HOUR = 2000 # цена за час работы бригады

def calc_color(square, price): # считаем количество банок краски и их цену
    total_color = square * COLOR # узнаем общее количество литров краски
    if total_color % ONE_COLOR > 0: # если есть остаток от деления, значит добавляем еще одну банку
        banka = total_color // ONE_COLOR + 1
    else:
        banka = total_color // ONE_COLOR # если нет, то не добавляем
    price *= banka
    return banka, price

def calc_hour(square): # считаем количество часов и их цену
    time = square * TIME # количество часов
    price = time * PRICE_OF_HOUR # цена за работу
    return time, price

def main():
    square = int(input('Площадь поверхности окрашиваемой стены : '))
    price_of_color = int(input('Цена 5-литровой емкости краски: '))
    banka, banka_price = calc_color(square, price_of_color)
    time, time_price = calc_hour(square)
    print(f"Количество требуемых емкостей краски: {banka:,}\n"
          f"Количество затраченных рабочих часов: {time:,.2f}\n"
          f"Стоимость краски: {banka_price:,.2f}$\n"
          f"Стоимость работы: {time_price:,.2f}$\n"
          f"Общая стоимость малярных работ: {time_price + banka_price:,.2f}$")

if __name__ == '__main__':
    main()
