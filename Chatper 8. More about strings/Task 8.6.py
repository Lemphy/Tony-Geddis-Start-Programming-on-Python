# 8.6 Среднее количество слов
def main():
    infile = open('text.txt','r')
    sentences = infile.readlines()
    infile.close()
    words = 0
    total = len(sentences)
    for i in sentences:
        words += len(i.split())
    print(f"Среднее количество слов в расчете на одно предложение: {words/total}.")

if __name__ == "__main__":
    main()
