# 6.3 Номера строк

def create_file_with_values():
    # Создаем файл с числами
    outfile = open('numbers.txt', 'w', encoding='UTF-8')
    for value in range(1, 101):
        outfile.write(f'{value}\n')
    outfile.close()

def check_user_filename():
    filename = input("Введите название файла: ")
    if filename == 'numbers.txt':
        reading()
    else:
        print('Файл не обнаружен.')

def reading():
    infile = open('numbers.txt', 'r', encoding='UTF-8')
    counter = 0
    for line in infile:
        line = line.rstrip()
        counter += 1
        print(f'{counter}: {line}')
    infile.close()

def main():
    create_file_with_values()
    check_user_filename()

if __name__ == '__main__':
    main()
