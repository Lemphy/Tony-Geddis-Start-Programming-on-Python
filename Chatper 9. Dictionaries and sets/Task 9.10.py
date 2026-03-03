# 9.10 Словарный индекс

def main():
    my_dict = dict()
    my_list = list()
    infile = open('Kennedy.txt','r')
    text_with_spaces = infile.readlines()
    infile.close()
    for i in range(len(text_with_spaces)): # проходим по i элементам списка
        text_split = text_with_spaces[i].rstrip().split() # вернуть список слов в строковом значении разделенных пробелами
        for x in range(len(text_split)): # проходим по списку слов в строке
            text_split[x] = text_split[x].lower().strip(',.!?()') # убираем из слова лишние символы и буквы в большом регистре
            if text_split[x] not in my_dict: # если отформатированное слово НЕ находится в словаре
                my_dict[text_split[x]] = [i+1] # добавляем в словарь ключ(слово) со значением строки в которой это слово найдено
            else: # если отформатированное слово уже есть в словаре
                if my_dict[text_split[x]][-1] != i+1: # если последний добавленный элемент в список не равняется текущей строке, то есть если символ повторился в строке дважды - мы его запишем только один раз
                    my_dict[text_split[x]].append(i+1) # получаем значение за ключом, применяем к значению метод добавления в конец списка

    for k in list(my_dict.keys()): # получаем список ключей словаря и проходим его
        my_list.append(k) # добавляем в список k ключ
    my_list.sort() # применяем сортировку ключей в алфавитном порядке
    outfile = open('Index.txt', 'w') # открываем файл вывода для записи
    for key in range(len(my_list)): # проходим список ключей в алфавитном порядке
        temp_string = f'{my_list[key]} : ' # создаем строку аккумулятор содержащую ключ
        for value in my_dict[my_list[key]]: # проходим список за значением, которое мы получили указав ключ
            temp_string += f"{str(value)} " # добавляем в строку аккумулятор значение из списка
        temp_string += '\n' # после окончания прохода списка добавляем символ новой строки
        outfile.write(temp_string) # записываем переменную аккумулятор в файл
    outfile.close()
    print('Файл успешно записан.')

if __name__ == "__main__":
    main()
