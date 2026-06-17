# 6.1 Вывод файла на экран
def main():
    # Создаем файл с числами
    outfile = open('numbers.txt', 'w', encoding= 'UTF-8')
    for value in range(1,101):
        outfile.write(f'{value}\n')
    outfile.close()

    # Выводим содержимое файла
    infile = open('numbers.txt', 'r', encoding= 'UTF-8')
    for value in infile:
        value = int(value.rstrip())
        print(value)
    print('Вывод окончен.')

if __name__ == '__main__':
    main()
