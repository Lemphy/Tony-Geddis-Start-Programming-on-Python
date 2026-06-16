# 5.16 Счетчик четных/нечетных чисел
import random

def main():
    even = 0 # четное
    odd = 0 # нечетное
    for i in range(100):
        temp = random.randint(1,100)
        if temp % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f'Количество четных: {even}\n'
          f'Количество не четных: {odd}')

if __name__ == '__main__':
    main()
