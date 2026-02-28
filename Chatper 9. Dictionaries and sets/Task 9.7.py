# 9.7 Победители мировой серии
def main():
    user_ans = get_user_ans()
    win_counts, year_names = create_dicts()
    if user_ans != 1904 and user_ans != 1994:
        print(f"В {user_ans} году выиграла команда {year_names[user_ans]}\n"
              f"Количество побед в Мировой серии: {win_counts[year_names[user_ans]]}")
    else:
        print("В этом году соревнования не проводились.")

def get_user_ans():
    while True:
        try:
            user_answer = int(input("Введите год в диапазоне между 1903 и 2009 годами\n>>> "))
            while user_answer < 1903 or user_answer > 2009:
                user_answer = int(input("Введите год в диапазоне между 1903 и 2009 годами\n>>> "))
        except ValueError:
            print('Ошибка значения.')
        else:
            return user_answer

def create_dicts():
    win_dct = dict()
    year_dct = dict()
    infile = open('WorldSeriesWinners.txt', 'r')
    text = infile.readlines()
    infile.close()
    year = 1903
    for i in range(len(text)):  # проходим i элементы списка text
        text[i] = text[i].rstrip()  # отсекаем пробельные символы с конца
        if text[i] not in f'World Series Not Played in {year}':  # если i элемент не является подстрокой
            if text[i] not in win_dct:  # если i элемента(ключа) нет в словаре
                win_dct[text[i]] = 1  # добавляем в словарь со значением 1
            else:  # если i элемент(ключ) уже есть в словаре
                win_dct[text[i]] += 1  # повышаем значение ключа на 1
            year_dct[year] = text[i]  # добавляем в словарь год:название i элемента(название команды)
            year += 1  # прибавляем год
        else:  # если i элемент оказался подстрокой, значит соревнований не было.
            year += 1
    return win_dct, year_dct

if __name__ == "__main__":
    main()
