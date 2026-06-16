# 5.20 Игра в угадывание случайного числа
import random

go_next = 'да'

def generate_random_value():
    return random.randint(1,10)

def check_answer_and_count(correct_value):
    counter = 0
    while True:
        answer = int(input('Введите рандомное число: '))
        counter += 1
        if answer == correct_value:
            print(f'Вы угадали! Поздравляем! Потрачено попыток: {counter}\nПродолжаем? (да/нет): ', end = '')
            global go_next
            go_next = input()
            return None
        elif answer < correct_value:
            print('Слишком мало, попробуйте еще раз!')
        elif answer > correct_value:
            print('Слишком много, попробуйте еще раз!')
        else:
            return None

def main():
    print('Игра угадай число!')
    while go_next == 'да':
        temp = generate_random_value()
        check_answer_and_count(temp)
    print('Игра завершена.')

if __name__ == '__main__':
    main()
