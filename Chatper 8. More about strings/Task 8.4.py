def main():
    text = input('Введите текст для конвертирования в азбуку морзе: ')
    print(convert_to_morze(text))

def convert_to_morze(value):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
    morse_codes = [
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
        "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
        "..-", "...-", ".--", "-..-", "-.--", "--..", ".----", "..---", "...--",
        "....-", ".....", "-....", "--...", "---..", "----.", "-----", " "]
    temp = ""
    for i in value:
        i = i.upper()
        if i in alphabet:
            temp += f'{morse_codes[alphabet.index(i)]} '
        else:
            print(f"Значения {i} не существует в азбуке морзе.")
    return temp

if __name__ == "__main__":
    main()
