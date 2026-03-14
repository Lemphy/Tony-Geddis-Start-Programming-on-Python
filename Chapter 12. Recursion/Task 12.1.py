# 12.1 Рекурсивная печать

def main():
    recursion(int(input("Введите число: ")))

def recursion(n: int):
    if n < 1: # базовый случай
        return
    else: # рекурсивный случай
        recursion(n - 1)
        print(n)

if __name__ == "__main__":
    main()
