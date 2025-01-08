import os

#Это надо переделать
class Car:
    def __init__(self, brand, model, year, color, mileage, price, is_stolen, max_speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage
        self.price = price
        self.is_stolen = is_stolen
        self.max_speed = max_speed

    def __str__(self):
        return f"{self.brand:<15} {self.model:<15} {self.year:<5} {self.color:<10} {self.mileage:<10} {self.price:<10} {'Да' if self.is_stolen else 'Нет':<5} {self.max_speed:<10}"


class CarDatabase:
    FILENAME = 'cars.txt'

    def __init__(self):
        self.cars = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.FILENAME):
            with open(self.FILENAME, 'r', encoding='utf-8') as file:
                for line in file:
                    brand, model, year, color, mileage, price, is_stolen, max_speed = line.strip().split('|')
                    self.cars.append(Car(
                        brand,
                        model,
                        int(year),
                        color,
                        int(mileage),
                        float(price),
                        is_stolen == 'Да',
                        float(max_speed)
                    ))

    def save_data(self):
        with open(self.FILENAME, 'w', encoding='utf-8') as file:
            for car in self.cars:
                file.write('|'.join([
                    car.brand,
                    car.model,
                    str(car.year),
                    car.color,
                    str(car.mileage),
                    str(car.price),
                    'Да' if car.is_stolen else 'Нет',
                    str(car.max_speed)
                ]) + '\n')

    def show_cars(self):
        if not self.cars:
            print("В базе данных нет автомобилей.")
            return

        print(f"{'Марка':<15} {'Модель':<15} {'Год':<5} {'Цвет':<10} {'Пробег':<10} {'Цена':<10} {'Угнан?':<5} {'Макс. Скор.':<10}")
        for i, car in enumerate(self.cars, start=1):
            print(f"{i}) {car}")

    def add_car(self):
        brand = input("Введите марку: ")
        model = input("Введите модель: ")
        year = int(input("Введите год выпуска: "))
        color = input("Введите цвет: ")
        mileage = int(input("Введите пробег: "))
        price = float(input("Введите цену: "))
        is_brand_new = input("Был было кражи? (1 - Да, 0 - Нет): ") == "1"
        max_speed = float(input("Введите максимальную скорость: "))

        new_car = Car(brand, model, year, color, mileage,
                      price, is_brand_new, max_speed)
        self.cars.append(new_car)
        print("Автомобиль добавлен.")
        self.save_data()

    def remove_car(self):
        self.show_cars()
        index = int(input("Введите номер машины для удаления: ")) - 1
        if 0 <= index < len(self.cars):
            self.cars.pop(index)
            print("Автомобиль удален.")
            self.save_data()
        else:
            print("Некорректный номер.")

    def search_car(self):
        criterion = input(
            "Введите значение для поиска (марка, модель, цвет): ")
        results = [car for car in self.cars if criterion in (
            car.brand, car.model, car.color)]

        if not results:
            print("Машины не найдены.")
            return

        print("Результаты поиска:")
        for car in results:
            print(car)

    def update_car(self):
        self.show_cars()
        index = int(input("Введите номер машины для изменения: ")) - 1
        if 0 <= index < len(self.cars):
            car = self.cars[index]
            column = int(input(
                "Введите номер столбца для изменения (1 - марка, 2 - модель, 3 - год, 4 - цвет, 5 - пробег, 6 - цена, 7 - угнан, 8 - макс. скорость): "))

            if column == 1:
                car.brand = input("Введите новую марку: ")
            elif column == 2:
                car.model = input("Введите новую модель: ")
            elif column == 3:
                car.year = int(input("Введите новый год выпуска: "))
            elif column == 4:
                car.color = input("Введите новый цвет: ")
            elif column == 5:
                car.mileage = int(input("Введите новый пробег: "))
            elif column == 6:
                car.price = float(input("Введите новую цену: "))
            elif column == 7:
                car.is_stolen = input(
                    "Находится ли в угоне (1 - Да, 0 - Нет): ") == "1"
            elif column == 8:
                car.max_speed = float(
                    input("Введите новую максимальную скорость: "))
            else:
                print("Некорректный номер столбца.")
                return

            print("Данные автомобиля обновлены.")
            self.save_data()
        else:
            print("Некорректный номер.")


def main():
    db = CarDatabase()
    while True:
        print("\nВыберите опцию:")
        print("1) Показать таблицу машин")
        print("2) Добавить машину")
        print("3) Убрать машину")
        print("4) Поиск машины")
        print("5) Изменить данные машины")
        print("6) Выход")

        choice = input("Ваш выбор: ")
        if choice == "1":
            db.show_cars()
        elif choice == "2":
            db.add_car()
        elif choice == "3":
            db.remove_car()
        elif choice == "4":
            db.search_car()
        elif choice == "5":
            db.update_car()
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, попробуйте еще раз.")


if __name__ == "__main__":
    main()
