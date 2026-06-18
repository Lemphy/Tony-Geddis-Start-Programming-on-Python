# 7.4 Программа анализа чисел
import random
MAX = 20

def main():
    random_list = []
    for value in range(MAX):
        temp_value = random.randint(1,100)
        random_list.append(temp_value)
    min_value = min(random_list)
    max_value = max(random_list)
    total = 0
    for i in random_list:
        total += i
    average = total / MAX
    print('Список:', *random_list)
    print(f"Наименьшее число в списке: {min_value}\n"
          f"Наибольшее число в списке: {max_value}\n"
          f"Сумма чисел в списке: {total}\n"
          f"Среднее арифметическое значение чисел в списке: {average:,.2f}\n")

if __name__ == '__main__':
    main()
