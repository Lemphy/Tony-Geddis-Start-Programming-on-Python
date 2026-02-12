YEAR = 1950

def main():
    array = get_difference_between_years()
    average = get_average_change_population(array)
    max_year = YEAR + array.index(max(array))+1
    min_year = YEAR + array.index(min(array))+1
    print(f"Средний прирост в год: {average}\n"
          f"Максимальный год с приростом: {max_year}\n"
          f"Минимальный год с приростом: {min_year}\n")

def get_array_from_file():
    infile = open("USPopulation.txt", 'r')
    array = infile.readlines()
    for i in range(len(array)):
        array[i] = int(array[i].rstrip())
    return array

def get_difference_between_years():
    array = get_array_from_file()
    temp = []
    for i in range(1, len(array)):
        temp.append(array[i] - array[i-1])
    return temp

def get_average_change_population(array):
    total = 0
    for i in array:
        total += i
    return total / len(array)

if __name__ == "__main__":
    main()
