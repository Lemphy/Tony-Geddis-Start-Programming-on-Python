def main():
    try:
        infile = open('WorldSeriesWinners.txt', 'r')
        winners = infile.readlines()
        infile.close()
        for i in range(len(winners)):
            winners[i] = winners[i].rstrip()
        name = input("Введите название команды для поиска: ")
        counter = 0
        if name not in winners:
            print("Данной команды нету в списке.")
        else:
            for i in winners:
                if i == name:
                    counter += 1
            print('Команда выиграла', counter, 'раз.')
    except:
        print("Ошибка.")

if __name__ == "__main__":
    main()
