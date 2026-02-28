# 9.5 Частота слов
def main():
    user_answer = get_user_answer()
    if user_answer == 1:
        show_dict_in_console()
    elif user_answer == 2:
        show_dict_in_file()

def menu():
    print('*' * 40)
    print(f'Выберите вариант отображения результата:\n'
          f'1 - Показать в консоли\n'
          f'2 - Записать в файл\n'
          f'3 - Завершить работу')

def get_user_answer():
    menu()
    answer = int(input("Введите выбранный пункт: "))
    while answer < 1 or answer > 3:
        answer = int(input("Введите выбранный пункт: "))
    return answer

def create_dict_with_counts(): # создаем словарь со словами и их количеством в тексте
    filename = input("Введите название файла (example.txt)\n>>> ")
    if filename.endswith('.txt'):
        infile = open(filename, 'r', encoding= 'UTF-8')
        text = infile.read().lower().split()  # получаем все содержимое файла в виде одной строки, преобразуем всю строку в маленькие символы, удаляем пробелы между словами и помещаем их в список
        infile.close()
        for i in range(len(text)):  # проходим список text
            text[i] = text[i].rstrip(',.!?')  # если в конце слова i есть один из символов (,.!?), то отсекаем их
        dct = dict()  # создаем пустой словарь
        for i in range(len(text)):  # проходим список text
            if text[i] not in dct:  # если i элемент списка text не находится в словаре
                dct[text[i]] = 1  # создаем в словаре ключ i и присваиваем ему значение 1
            else:  # если i элемент списка text уже находится в словаре
                dct[text[i]] += 1  # прибавляем 1 к значению ключа i
        return dct  # возвращаем ссылку на словарь
    else:
        print(f"Файл {filename} не найден.")
    return None

def show_dict_in_console(): # вывести содержимое словаря в консоль
    temp = create_dict_with_counts()
    if temp is not None:
        maximum = get_key_max_length(temp) # определяем самый длинный ключ в словаре
        i = 1
        for k, v in temp.items():
            print(f"{i:>3}.{k:<{maximum+1}}:{v:<20}")
            i += 1
    else:
        print('Error.')

def get_key_max_length(arg): # определяем самый длинный ключ в словаре
    return max([len(j) for j in arg])

def show_dict_in_file(): # вывести содержимое словаря в файл
    temp = create_dict_with_counts()
    if temp is not None:
        maximum = get_key_max_length(temp) # определяем самый длинный ключ в словаре
        filename = 'output.txt'
        outfile = open(filename, 'w', encoding= 'UTF-8')
        i = 1
        for k, v in temp.items():
            outfile.write(f"{i:>3}.{k:<{maximum+1}}:{v:<20}\n") # записываем в файл текущий результат k, v
            i += 1
        outfile.close()
        print(f"Файл {filename} успешно записан в корневой директории проекта.")
    else:
        print("Error.")

if __name__ == "__main__":
    main()
