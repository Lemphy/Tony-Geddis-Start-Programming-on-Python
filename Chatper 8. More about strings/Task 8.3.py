def main():
    print(create_normal_date())

def create_normal_date():
    normal_date = check_correct_day_year_and_month()
    months = [
        "Января", "Февраля", "Марта", "Апреля",
        "Мая", "Июня", "Июля", "Августа",
        "Сентября", "Октября", "Ноября", "Декабря"]
    normal_date[1] = months[normal_date[1] - 1]
    temp = ''
    for i in range(len(normal_date)):
        if i == 0 or i == 1:
            temp += f"{normal_date[i]} "
        else:
            temp += f"{normal_date[i]} г."
    return temp

def check_correct_day_year_and_month():
    while True:
        try:
            temp = check_inputting()
            while temp[0] < 1 or temp[0] > 31:
                print('Ошибка в дне!')
                temp = check_inputting()
            while temp[1] < 1 or temp[1] > 12:
                print('Ошибка в месяце!')
                temp = check_inputting()
        except ValueError:
            print("Некорректное значение.")
        else:
            return temp

def check_inputting():
    date = input("Введите дату в формате dd/mm/yyyy: ")
    temp = date.split('/')
    return [int(i) for i in temp]

if __name__ == "__main__":
    main()
