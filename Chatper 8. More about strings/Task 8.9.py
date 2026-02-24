# 8.9 Гласные и согласные
VOWELS_LIST = ('а', 'о', 'у', 'ы', 'э', 'е', 'ё', 'и', 'ю', 'я') # кортеж гласных букв
def main():
    sentence = input("Введите предложение для определения в нем количества гласных и согласных букв\n>>> ")
    vowels, consonants = check_vowels_and_consonants(arg = sentence)
    print(f"Количество гласных: \t{vowels}\n"
          f"Количество согласных: \t{consonants}")

def check_vowels_and_consonants(arg):
    counter_vowels = 0 # гласные
    counter_consonants = 0 # согласные
    for i in arg.lower(): # пройтись по каждому символу строки
        if i.isalpha(): # определить является ли символ буквой
            if i in VOWELS_LIST: # если буква есть в кортеже гласных букв, то добавить в счетчик гласных +1
                counter_vowels += 1
            else: # если буквы нет в кортеже гласных, значит она согласная, добавляем в счетчик согласных +1
                counter_consonants += 1
    return counter_vowels, counter_consonants

if __name__ == "__main__":
    main()
