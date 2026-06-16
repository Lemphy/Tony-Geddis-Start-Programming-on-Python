# 5.21 Игра "Камень, ножницы, бумага"
import random

ROCK = 'камень'
SCISSORS = 'ножницы'
PAPER = 'бумага'
USER_WIN = 1
COMPUTER_WIN = 2

def create_answer(answer):
    if answer == 1 or answer == ROCK:
        return ROCK
    elif answer == 2 or answer == SCISSORS:
        return SCISSORS
    elif answer == 3 or answer == PAPER:
        return PAPER
    else:
        return None

def check_winner():
    while True:
        temp = random.randint(1, 3)
        computer = create_answer(temp)
        user = create_answer(input('Ваш выбор: камень, ножницы, бумага?\nОтвет: '))
        print(computer, user)
        if computer == user:
            print('Оба игрока сделали одинаковый выбор. Переигровка.')
        elif computer == ROCK:
            if user == SCISSORS:
                return COMPUTER_WIN
            else:
                return USER_WIN
        elif computer == SCISSORS:
            if user == ROCK:
                return USER_WIN
            else:
                return COMPUTER_WIN
        elif computer == PAPER:
            if user == ROCK:
                return COMPUTER_WIN
            else:
                return USER_WIN

def main():
    go_next = 'да'
    while go_next == 'да':
        winner = check_winner()
        if winner == COMPUTER_WIN:
            print('Выиграл компьютер')
        elif winner == USER_WIN:
            print('Выиграл пользователь')
        else:
            print('Error')
        go_next = input('Продолжаем? (да/нет): ')

if __name__ == '__main__':
    main()
