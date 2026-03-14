# 12.3 Рекурсивные строки

def main():
    recursion_strings(arg = 5)

def recursion_strings(arg):
    if arg == 0: # базовый случай
        return None
    else: # рекурсивный случай
        recursion_strings(arg - 1)
        print(arg * '*')
        return None

if __name__ == "__main__":
    main()
