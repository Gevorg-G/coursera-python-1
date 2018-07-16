"""
Парсер CSV-файла с описанием машин для курса "Погружение в Python"
https://www.coursera.org/learn/diving-in-python/programming/bd6aI/klassy-i-nasliedovaniie
"""
import os
import csv


class BaseCar:
    """
    Базовый класс для описания машин.
    Содержит: тип машины, бренд, фото, грузоподъёмность
    """

    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        """Метод получает расширения файла фото"""
        return os.path.splitext(self.photo_file_name)[1]


class Car(BaseCar):
    """
    Дочерний класс, описывающий машины типа Car.
    В дополнение к базовому класс BaseCar добавлен атрибут количества мест в машине.
    """

    def __init__(self, car_type, brand, photo_file_name, carrying,
                 passenger_seats_count):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(BaseCar):
    """
    Дочерний класс, описывающий машины типа Truck.
    В дополнение к базовому класс BaseCar добавлены атрибуты длины, ширины и высоты.
    """

    def __init__(self, car_type, brand, photo_file_name, carrying,
                 body_width, body_height, body_length):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.body_width = body_width
        self.body_height = body_height
        self.body_length = body_length

    def get_body_volume(self):
        """"Метод вычисляет объём кузова"""
        return self.body_width * self.body_height * self.body_length


class SpecMachine(BaseCar):
    """
    Дочерний класс, описывающий машины типа SpecMachine.
    В дополнение к базовому класс BaseCar добавлен атрибут дополнительных фич.
    """

    def __init__(self, car_type, brand, photo_file_name, carrying,
                 extra):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.extra = extra


def create_car(row):
    if len(row) != 7:
        # raise ValueError("Lenght of row is wrong")
        return None

    car_type = row[0]
    car_brand = row[1]
    car_seats = row[2]
    car_photo = row[3]
    car_whl = row[4]
    car_carrying = row[5]
    car_extra = row[6]

    if car_type not in ['car', 'truck', 'spec_machine']:
        # raise ValueError("Wrong type of car")
        return None
    if car_brand == '':
        # raise ValueError("Required value 'brand' is missing")
        return None
    if car_carrying == '':
        # raise ValueError("Required value 'carrying' is missing")
        return None

    if car_type == 'car':
        if car_seats == '':
            # raise ValueError(
            #     "Required value 'passenger_seats_count' is missing")
            return None
        return Car(car_type, car_brand, car_photo, float(car_carrying), int(car_seats))

    if car_type == 'truck':
        if car_whl == '':
            car_width = 0.0
            car_height = 0.0
            car_length = 0.0
        else:
            car_whl_splitted = car_whl.split('x')
            if len(car_whl_splitted) != 3:
                car_width = 0.0
                car_height = 0.0
                car_length = 0.0
            else:
                try:
                    car_width = float(car_whl_splitted[0])
                    car_height = float(car_whl_splitted[1])
                    car_length = float(car_whl_splitted[2])
                except ValueError:
                    # print("Wrong data about whl")
                    return None
        return Truck(car_type, car_brand, car_photo, float(car_carrying), car_width, car_height, car_length)

    if car_type == 'spec_machine':
        return SpecMachine(car_type, car_brand, car_photo, float(car_carrying), car_extra)

    return None


def get_car_list(csv_filename):
    """Обрабатывает входящий csv-файл"""
    car_list = []
    if os.path.exists(csv_filename) and os.path.getsize(csv_filename) > 0:
        with open(csv_filename) as csv_fd:
            reader = csv.reader(csv_fd, delimiter=';')
            next(reader)  # пропускаем заголовок
            for row in reader:
                # print(row)
                if create_car(row) != None:
                    car_list.append(create_car(row))

    return car_list
