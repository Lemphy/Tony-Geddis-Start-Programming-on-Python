# 12.4 Максимальное значение в списке
import random

def main():
    mylist = list()
    for i in range(5):
        mylist.append(random.randint(1,10))
    print(mylist)
    print(f"Максимальное значение без рекурсии {max(mylist)}")
    print(f"Максимальное значение в списке {maximal_value(temp_list = mylist)}")

def maximal_value(temp_list): # передаем список
    n = len(temp_list) # присваиваем длину списка
    if n == 1: # если длина списка 1
        return temp_list[n-1] # берем элемент под индексом длина списка - 1
    else: # если длина списка не больше 1
        temp = maximal_value(temp_list[0 : n - 1]) # вызываем рекурсию, которая берет срез списка на 1 элемент меньше, присваиваем значению temp результат
        if temp > temp_list[n - 1]: # если результат больше последнего элемента списка, возвращаем результат
            return temp
        else: # если результат меньше последнего элемента списка, присваиваем результату последний элемент списка
            return temp_list[n - 1]

if __name__ == "__main__":
    main()
