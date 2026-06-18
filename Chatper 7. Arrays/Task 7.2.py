# 7.2 Генератор лотерейных чисел
import random

COUNT = 7

def main():
    random_list = []
    for value in range(COUNT):
        random_list.append(random.randint(0,9))
    for value in random_list:
        print(f'{value}', end = ' ')

if __name__ == '__main__':
    main()
