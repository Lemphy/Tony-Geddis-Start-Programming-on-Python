# 6.5 Сумма чисел

def create_file_with_values():
    # Создаем файл с числами
    outfile = open('numbers.txt', 'w', encoding='UTF-8')
    for value in range(1, 101):
        outfile.write(f'{value}\n')
    outfile.close()

def main():
    create_file_with_values()
    counter = 0
    infile = open('numbers.txt', 'r', encoding= 'UTF-8')
    for line in infile:
        line = int(line.rstrip())
        counter += line
    print(f'Сумма чисел: {counter}')
    infile.close()

if __name__ == '__main__':
    main()
