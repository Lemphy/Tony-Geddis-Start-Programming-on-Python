# 5.15 Средний бал и его уровень

def calc_average(s1, s2, s3, s4, s5): # функция расчета среднего балла
    return (s1 + s2 + s3 + s4 + s5) / 5

def determine_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    score1 = check_correct_score('Введите оценку 1: ')
    score2 = check_correct_score('Введите оценку 2: ')
    score3 = check_correct_score('Введите оценку 3: ')
    score4 = check_correct_score('Введите оценку 4: ')
    score5 = check_correct_score('Введите оценку 5: ')
    average_score = calc_average(score1, score2, score3, score4, score5)
    grade = determine_grade(average_score)
    print(f'Средняя оценка: {average_score}\n'
          f'Буквенная оценка: {grade}')

def check_correct_score(arg):
    score = int(input(arg))
    while score < 0 or score > 100:
        print('Некорректная оценка!')
        score = int(input(arg))
    return score

if __name__ == '__main__':
    main()
