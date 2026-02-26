# 9.1 Информация об учебных курсах
def main():
    dct = {'CS101':{'number': '3004', 'teacher': 'Хайнс', 'time': '8:00'},
            'CS102':{'number':'4501', 'teacher': 'Альварадо', 'time': '9:00'},
            'CS103':{'number': '6755', 'teacher': 'Рич', 'time': '10:00'},
            'NT110': {'number': '1244', 'teacher': 'Берк', 'time': '11:00'},
            'CM241': {'number': '1411', 'teacher': 'Ли', 'time': '13:00'}}
    user_ans = input("Введите номер курса для поиска\n>>> ")
    if user_ans in dct:
        print(f"Курс: {user_ans}\n"
              f"Номер аудитории: {dct[user_ans]['number']}\n"
              f"Преподаватель: {dct[user_ans]['teacher']}\n"
              f"Время: {dct[user_ans]['time']}")
    else:
        print(f"Курс не найден.")

if __name__ == "__main__":
    main()
