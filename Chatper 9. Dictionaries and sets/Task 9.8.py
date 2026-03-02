# 9.8 Имена и адреса электронной почты
import pickle

FIND = 1
CREATE_NEW = 2
CHANGE = 3
REMOVE = 4
LOOK = 5
QUIT = 6

def main():
    mydict = start()
    while True:
        show_menu()
        user_answer = get_digit_answer()
        if user_answer == FIND:
            find_email_user(mydict)
        elif user_answer == CREATE_NEW:
            create_new_name_email(mydict)
        elif user_answer == CHANGE:
            change_email_by_name(mydict)
        elif user_answer == LOOK:
            look(mydict)
        elif user_answer == REMOVE:
            delete_name_and_email(mydict)
        elif user_answer == QUIT:
            quit_and_save_dict(mydict)
            break

def show_menu(): # показать пункты меню
    print(f"{'*' * 44}\n"
          f"Выберите нужный пункт меню.\n"
          f"1. Найти почту по имени\n"
          f"2. Добавить новое имя и почту\n"
          f"3. Изменить адрес электронной почты по имени\n"
          f"4. Удалить имя и почту\n"
          f"5. Показать содержимое словаря\n"
          f"6. Закончить работу.")

def get_digit_answer(): # получить корректный ответ от пользователя при выборе пункта меню
    while True:
        try:
            answer = int(input('Ответ: '))
            while answer < FIND or answer > QUIT:
                answer = int(input('Ответ: '))
        except ValueError:
            print("Некорректное значение.")
        else:
            return answer

def get_menu_answer(text):
    if text == 'Введите имя: ':
        while True:
            name = input(text)
            if not name.isdigit():
                temp = name[:1].upper() + name[1:].lower()
                return temp
            else:
                print('В имени должны быть только буквы алфавита.')
    elif text == 'Введите почту: ':
        while True:
            email = input(text)
            if "@" in email and '.' in email: # если в эмейле есть собачка и точка
                return email.lower()
            else:
                print("Эмейл адрес должен содержать @ и точку.")
    return None

def find_email_user(temp_dict): # 1. Найти почту по имени
    name = get_menu_answer('Введите имя: ')
    key = temp_dict.get(name, 'Имя не найдено.')
    if name in temp_dict:
        print(f'У {name} почта {key}')
    else:
        print(key)

def create_new_name_email(temp_dict): # 2. Добавить новое имя и почту
    name = get_menu_answer('Введите имя: ')
    email = get_menu_answer('Введите почту: ')
    if name not in temp_dict:
        temp_dict[name] = email
        print(f'Имя {name} и почта {email} успешно добавлены.')
    else:
        print("Данное имя уже есть в списке. Чтобы изменить почту для данного имени выберите пункт меню - 3.")

def change_email_by_name(temp_dict): # 3. Изменить адрес электронной почты по имени
    name = get_menu_answer('Введите имя: ')
    if name in temp_dict:
        email = get_menu_answer('Введите почту: ')
        temp_dict[name] = email
        print(f"Эмейл адрес пользователя {name} успешно изменен на {email}")
    else:
        print('Указанное имя не обнаружено в списке.')

def delete_name_and_email(temp_dict): # 4. Удалить имя и почту
    name = get_menu_answer('Введите имя: ')
    if name in temp_dict:
        email = temp_dict.pop(name)
        print(f"Имя пользователя {name} и его почта {email} успешно удалены.")
    else:
        print('Указанное имя не обнаружено в списке.')

def look(temp_dict): # показать содержимое словаря
    if temp_dict:
        for k, v in temp_dict.items():
            print(f"{k}:{v}")
    else:
        print("Словарь пуст.")

def start():
    try:
        infile = open('dictionary.txt', 'rb')
        temp_dict = pickle.load(infile)
        infile.close()
    except FileNotFoundError: # если мы не смогли найти файл, то просто создаем пустой словарь
        temp_dict = dict()
    return temp_dict # возвращаем ссылку на словарь

def quit_and_save_dict(temp_dict): # выйти из программы и законсервировать словарь
    outfile = open('dictionary.txt','wb')
    pickle.dump(temp_dict,outfile)
    outfile.close()
    print("Программа успешно закрыта.")

if __name__ == "__main__":
    main()
