# 6.9 Обработка исключений

def create_file_with_values():
    # Создаем файл с числами
    outfile = open('numbers.txt', 'w', encoding='UTF-8')
    for value in range(1, 101):
        outfile.write(f'{value}\n')
    outfile.close()

def main():
    create_file_with_values()
    try:
        filename = input('Введите имя файла (example.txt): ')
        outfile = open(filename, 'r', encoding='UTF-8')
        counter = 0
        total = 0
        for line in outfile:
            line = int(line.rstrip())
            counter += 1
            total += line
    except IOError:
        print(f'Файл {filename} не обнаружен')
    except ValueError:
        print(f'Некорректная строка в файле. Содержимое строки {counter}: {line}')
    else:
        print(f"Общая сумма чисел: {total}\n"
              f"Количество чисел: {counter}\n"
              f"Среднее арифметическое: {total/counter}")

if __name__ == '__main__':
    main()
