# 6.12 Среднее количество шагов
JAN_DAYS = 31
FEB_DAYS = 28
MARCH_DAYS = 31
APRIL_DAYS = 30
MAY_DAYS = 31
JUNE_DAYS = 30
JULY_DAYS = 31
AUG_DAYS = 31
SEPT_DAYS = 30
OCT_DAYS = 31
NOV_DAYS = 30
DEC_DAYS = 31

def main():
    infile = open('steps.txt', 'r', encoding = 'UTF-8')
    show_month(infile, 'январе', JAN_DAYS)
    show_month(infile, 'феврале', FEB_DAYS)
    show_month(infile, 'марте', MARCH_DAYS)
    show_month(infile, 'апреле', APRIL_DAYS)
    show_month(infile, 'мае', MAY_DAYS)
    show_month(infile, 'июне', JUNE_DAYS)
    show_month(infile, 'июле', JULY_DAYS)
    show_month(infile, 'августе', AUG_DAYS)
    show_month(infile, 'сентябре', SEPT_DAYS)
    show_month(infile, 'октябре', OCT_DAYS)
    show_month(infile, 'ноябре', NOV_DAYS)
    show_month(infile, 'декабре', DEC_DAYS)
    infile.close()

def show_month(file,month, days):
    total = 0
    for day in range(days):
        steps = int(file.readline())
        total += steps
    avg = total / days
    print(f'Среднее количество шагов в {month} составило {avg:,.0f}')

if __name__ == '__main__':
    main()
