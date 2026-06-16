#5.11 Математический тест
import random

def check_answer(arg1, arg2):
    go_next = 'д'
    while go_next == 'д':
        def show_values():
            print(f"{arg1:^3}\n"
                  f"{'+':^3}\n"
                  f"{arg2:^3}\n")
        show_values()
        answer = int(input('Ответ: '))
        temp = arg1 + arg2
        if answer == temp:
            print('Правильно!')
            go_next = input('Продолжаем? (д/н): ')
        else:
            print(f'Не правильно! Верный ответ: {temp}')
            go_next = input('Продолжаем? (д/н): ')
        arg1 = random.randint(100,500)
        arg2 = random.randint(100,500)

def main():
    val1 = random.randint(100,500)
    val2 = random.randint(100,500)
    check_answer(arg1 = val1, arg2 = val2)
    print('Работа окончена.')

if __name__ == '__main__':
    main()
