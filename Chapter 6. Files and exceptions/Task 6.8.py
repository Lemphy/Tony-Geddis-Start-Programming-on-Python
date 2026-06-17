# 6.8 Программа чтения файла со случайными числами
import random

def create_file_with_values(counter):
    # Создаем файл с числами
    outfile = open('numbers.txt', 'w', encoding='UTF-8')
    for i in range(counter):
        outfile.write(f'{random.randint(1,500)}\n')
    outfile.close()

def main():
    counter = int(input('Введите количество желаемых рандомных значений в файле: '))
    create_file_with_values(counter)
    outfile = open('numbers.txt', 'r', encoding='UTF-8')
    total = 0
    counter = 0
    for number in outfile:
        number = int(number.rstrip())
        total += number
        counter += 1
        print(number, end = ' ')
    print()
    outfile.close()
    print(f'Сумма чисел: {total}\n'
          f'Количество случайных чисел, прочитанных из файла: {counter}\n'
          f'Среднее значение: {total/counter}')

if __name__ == '__main__':
    main()
