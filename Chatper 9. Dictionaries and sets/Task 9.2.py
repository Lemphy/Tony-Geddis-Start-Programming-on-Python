# 9.2 Викторина со столицами
import random

def main():
    countries_capitals = {
        "Россия": "Москва",
        "Франция": "Париж",
        "Германия": "Берлин",
        "Япония": "Токио",
        "Казахстан": "Астана",
        "Италия": "Рим",
        "Великобритания": "Лондон"
    }
    true_answer = 0
    false_answer = 0
    go_next = 'д'
    while go_next.lower() == 'д':
        k,v = random.choice(list(countries_capitals.items()))
        user_answer = input(f"Введите столицу страны {k}\n>>> ")
        if user_answer[:1].upper() + user_answer[1:].lower() == v: # если пользователь ввел столицу в другом регистре
            print('Верно!')
            true_answer += 1
        else:
            print('Неправильно!')
            false_answer += 1
        print(f'Продолжаем? (д/н): ',end='')
        go_next = input()
    print(f"Правильных ответов: {true_answer}\n"
          f"Неправильных ответов: {false_answer}")

if __name__ == "__main__":
    main()
