# 10.2 Класс Car

class Car:
    def __init__(self, year, make):
        self.__year = year
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            print("Скорость не может быть отрицательной.")

    def get_speed(self):
        return self.__speed

def main():
    mycar = Car(2008, 'BMW')
    for i in range(5):
        mycar.accelerate()
        print(mycar.get_speed())
    for x in range(5):
        mycar.brake()
        print(mycar.get_speed())

if __name__ == "__main__":
    main()
