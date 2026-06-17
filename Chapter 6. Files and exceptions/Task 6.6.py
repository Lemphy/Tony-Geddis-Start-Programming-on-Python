# 6.6 Среднее арифметическое чисел

def create_file_with_values():
    # Создаем файл с числами
    outfile = open('numbers.txt', 'w', encoding='UTF-8')
    for value in range(1, 101):
        outfile.write(f'{value}\n')
    outfile.close()

def main():
    outfile = open('numbers.txt', 'r', encoding='UTF-8')
    counter = 0
    total = 0
    for line in outfile:
        line = int(line.rstrip())
        counter += 1
        total += line
    print(f"Общая сумма чисел: {total}\n"
          f"Количество чисел: {counter}\n"
          f"Среднее арифметическое: {total/counter}")

if __name__ == '__main__':
    main()
