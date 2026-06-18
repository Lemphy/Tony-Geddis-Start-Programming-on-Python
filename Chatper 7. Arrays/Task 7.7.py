# 7.7 Экзамен на получение водительских прав

def main():
    solution = ['A', 'C', 'A', 'A', 'D',
                'B', 'C', 'A', 'C', 'B',
                'A', 'D', 'C', 'A', 'D',
                'C', 'B', 'B', 'D', 'A']
    infile = open('student_solution.txt', 'r', encoding= 'UTF-8')
    answer_from_student = infile.readlines()
    infile.close()
    for i in range(len(answer_from_student)):
        answer_from_student[i] = answer_from_student[i].rstrip()
    correct = 0
    incorrect = 0
    incorrect_ans = []
    for k in range(len(answer_from_student)):
        if solution[k] == answer_from_student[k]:
            correct += 1
        else:
            incorrect += 1
            incorrect_ans.append(str(k + 1))
    print(f'Правильные ответы: {correct}, не правильные: {incorrect}')
    if correct >= 15:
        print(f'Поздравляем! Вы сдали экзамен с {correct}/20 верными ответами')
    else:
        print(f'Вы не сдали экзамен. Правильных ответов - {correct}, не правильных - {incorrect}')
    if incorrect > 0:
        print('Номера вопросов на которые ответили неправильно: ', end = '')
        for i in incorrect_ans:
            print(f'{i}', end = ' ')

if __name__ == '__main__':
    main()
