# 8.2 Сумма цифр в строке
def main():
    val = input("Введите ряд чисел без разделителей: ")
    print(f"Сумма чисел в строковом значении: {calculate_sum(value = val)}")
    print(f"Сумма чисел в строковом значении: {calculate_sum_1(value=val)}")

def calculate_sum(value): # 1 вариант
    temp = 0
    for i in value:
        temp += int(i)
    return temp

def calculate_sum_1(value): #2 вариант
    temp = [int(i) for i in value]
    return sum(temp)

if __name__ == "__main__":
    main()
