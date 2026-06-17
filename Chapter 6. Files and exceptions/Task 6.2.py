# 6.2 Вывод на экран верхей части файла
def main():
    # Создаем файл с числами
    outfile = open('numbers.txt', 'w', encoding= 'UTF-8')
    for value in range(1,101):
        outfile.write(f'{value}\n')
    outfile.close()

    # Выводим содержимое файла
    error_find = False
    while not error_find:
        user_file = input('Введите имя файла (example.txt): ')
        try:
            user_counter = int(input('Сколько строк нужно вывести: '))
        except ValueError:
            print('Ошибка.')
        else:
            error_find = True
            if user_file == 'numbers.txt':
                infile = open('numbers.txt', 'r', encoding= 'UTF-8')
                counter = 0
                for value in infile: # проходим файл построчно
                    if user_counter != counter: # если счетчик не равен нужному числу строк
                        value = int(value.rstrip())
                        print(value)
                        counter += 1
                    else: # если нужное число строк достигнуто, выходим из цикла, для экономии времени выполнения
                        break
                infile.close()
                print('Вывод окончен.')
            else:
                print('Файл не обнаружен')

if __name__ == '__main__':
    main()
