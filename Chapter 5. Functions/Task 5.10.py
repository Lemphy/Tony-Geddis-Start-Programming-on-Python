# 5.10 Футы в дюймы
FEET = 12

def feet_to_inches(val):
    return val * FEET

def main():
    inch = float(input('Введите количество футов для преобразования в дюймы: '))
    print(f"Футов: {inch:,.2f} - Дюймов: {feet_to_inches(inch):,.2f}")

if __name__ == '__main__':
    main()
