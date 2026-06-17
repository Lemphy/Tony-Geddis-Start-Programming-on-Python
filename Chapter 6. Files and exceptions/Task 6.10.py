# 6.10 Очки в игре в гольф

ENTER = 1
CHECK_FILE = 2

def enter_player_and_score(player, score):
    outfile = open('golf.txt', 'a', encoding = 'UTF-8')
    outfile.write(f'Имя игрока: {player}\n')
    outfile.write(f'Счет: {score}\n')
    outfile.write(f'\n')
    outfile.close()

def check_correct_input_to_file():
    player = input('Введите имя игрока: ')
    while True:
        try:
            score = int(input(f'Введите счет {player} в игре: '))
            while score < 0:
                print('Счет не может быть меньше нуля.')
                score = int(input(f'Введите счет {player} в игре: '))
        except ValueError:
            print('Некорректный счет')
        else:
            return player, score

def enter_to_file(): # ввод данных в файл
    go_next = 'д'
    while go_next == 'д':
        player, score = check_correct_input_to_file()
        enter_player_and_score(player=player, score=score)
        go_next = input('Ввести еще? (д/н): ')

def check_file(): # чтение файла
    try:
        infile = open('golf.txt', 'r', encoding = 'UTF-8')
    except IOError:
        print('Файл не обнаружен')
    else:
        name = infile.readline()
        if name != '':
            while name != '':
                name = name.rstrip()
                score = infile.readline().rstrip()
                infile.readline()
                print(f'{name}\n'
                      f'{score}\n')
                name = infile.readline()
            print('Чтение из файла окончено')
        else:
            print('Файл пуст')
        infile.close()

def main():
    print('Режим работы: 1 - ввести игрока и его счет\n'
          'Режим работы: 2 - проверить содержимое файла\n'
          'Любое другое значение для выхода')
    try:
        mode = int(input('Ответ: '))
    except ValueError:
        print('Ошибка')
    else:
        if mode == 1:
            enter_to_file()
        elif mode == 2:
            check_file()
        else:
            print('Завершение работы')

if __name__ == '__main__':
    main()
