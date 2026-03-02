# 9.9 Имитация игры в блек-джек
import random
MAX = 21

def main():
    dct = create_deck()
    mylist = dealing_cards(dct)
    check_winner(mylist)

def create_deck(): # создать словарь с названиями карт(ключ) их числами (значениями)
    card_suits = ('черви', 'пики', 'бубны', 'крестей') # масти карт
    card_meanings = ('валет', 'дама', 'король', 'туз', '2', '3','4','5','6','7','8','9','10') # значения карт
    numerical_value = {'валет': 10, 'дама': 10, 'король': 10, 'туз': 1}
    temp_dict = dict()
    for s in range(len(card_suits)): # проходим масти карт
        for m in range(len(card_meanings)): # проходим значения карт
            if card_meanings[m].isalpha(): # если значение карты это слово, а не цифра (валет, дама, король, туз)
                temp_dict[f"{card_meanings[m]} {card_suits[s]}"] = numerical_value[card_meanings[m]] # добавляем в словарь ключ [m + s] со значением m относящееся к словарю numerical_value
            else: # если значение карты это цифра (2 - 11)
                temp_dict[f"{card_meanings[m]} {card_suits[s]}"] = int(card_meanings[m]) # добавляем в словарь ключ [m + s] со значением m, преобразованное в целое число
    return temp_dict

def dealing_cards(temp_dict): # раздать карточки до победного
    players = {'Игрок_1': 0, 'Игрок_2': 0}
    check = False # булевая переменная для проверки дошел ли кто-то до MAX числа
    while temp_dict and not check: # пока в словаре есть хоть что-то и мы не нашли проигравшего
        for i in players: # проходим по словарю
            rand_key = random.choice(list(temp_dict)) # берем рандомный ключ из списка ключей словаря
            rand_value = temp_dict.pop(rand_key) # находим значение по ключу и удаляем пару ключ:значение
            if 'туз' in rand_key: # если рандомная карта это туз (число 1)
                bonus = rand_value + 10 # число 11
                if players[i] + bonus < MAX: # если при добавлении туза у игрока не превысится лимит в 21 очко, то добавляем значение туза из словаря + 10
                    players[i] += bonus
                    if players[i] >= MAX: # если i игрок дошел до MAX числа
                        check = True # флаг для выхода из цикла while
                        break # выходим из цикла for
                    print(f"Игроку {i} сдана карта {rand_key} со значением {rand_value}")
                else: # если при добавлении туза у игрока превысится лимит в 21 очко, то добавляем значение туза из словаря
                    players[i] += rand_value
                    if players[i] >= MAX:  # если i игрок дошел до MAX числа
                        check = True  # флаг для выхода из цикла while
                        break  # выходим из цикла for
                    print(f"Игроку {i} сдана карта {rand_key} со значением {rand_value}")
            else: # если рандомная карта отличается от туза
                players[i] += rand_value
                if players[i] >= MAX:  # если i игрок дошел до MAX числа
                    check = True  # флаг для выхода из цикла while
                    break  # выходим из цикла for
                print(f"Игроку {i} сдана карта {rand_key} со значением {rand_value}")
    return players

def check_winner(temp_dict):
    (name1, score1), (name2,score2) = temp_dict.items() # создаем список кортежей и присваиваем каждый кортеж переменным
    if score1 > score2:
        print(f"Побеждает {name2} со счетом {score2}\n"
              f"{name1} раньше достиг {MAX}.")
    elif score1 < score2:
        print(f"Побеждает {name1} со счетом {score1}\n"
              f"{name2} раньше достиг {MAX}.")
    else:
        print("У обоих игроков одинаковое количество очков. Ничья.")

if __name__ == "__main__":
    main()
