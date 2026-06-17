# 6.7 Программа записи файла со случайными числами
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
    for number in outfile:
        number = int(number.rstrip())
        print(number, end = ' ')
    outfile.close()

if __name__ == '__main__':
    main()
