# 7.13 Магический шар
import random

def main():
    infile = open('8ball.txt', 'r', encoding='UTF-8')
    answers = infile.readlines()
    infile.close()
    for i in range(len(answers)):
        answers[i] = answers[i].rstrip()
    while True:
        question = input("Вопрос: ")
        print(random.choice(answers))
        print('Продолжаем? (д/н):', end = " ")
        ans = input()
        while ans != 'д' and ans != 'н':
            print("Некорректное значение!")
            print('Продолжаем? (д/н):', end=" ")
            ans = input()
        if ans == 'н':
            break

if __name__ == "__main__":
    main()
