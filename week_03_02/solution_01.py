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

    @property
    def get_photo_file_ext(self):
        """Метод получает расширения файла фото"""
        ext = os.path.splitext(self.photo_file_name)[1]
        return ext


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
                 body_whl=0):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.body_whl = body_whl

    @property
    def get_body_volume(self):
        """"Метод вычисляет объём кузова"""
        whl = self.body_whl.split("x")
        return float(whl[0]) * float(whl[1]) * float(whl[2])


class SpecMachine(BaseCar):
    """
    Дочерний класс, описывающий машины типа SpecMachine.
    В дополнение к базовому класс BaseCar добавлен атрибут дополнительных фич.
    """

    def __init__(self, car_type, brand, photo_file_name, carrying,
                 extra):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.extra = extra


def create_car(row, car_list):
    """Создаёт объект класса Car"""
    try:
        car_type = row[0]
        car_brand = row[1]
        if row[2] == '':
            car_seats = 0
        else:
            car_seats = int(row[2])
        car_photo = row[3]
        car_carrying = float(row[5])
    except ValueError:
        print("Неверный формат данных, пропускаю: {}".format(car_brand))
    else:
        return car_list.append(
            Car(car_type, car_brand, car_photo, car_carrying, car_seats))


def create_truck(row, car_list):
    """Создаёт объект класса Truck"""
    try:
        car_type = row[0]
        car_brand = row[1]
        car_photo = row[3]
        car_whl = convert_whl(row[4])
        car_carrying = float(row[5])
    except ValueError:
        print("Неверный формат данных, пропускаю")
    else:
        return car_list.append(
            Truck(car_type, car_brand, car_photo, car_carrying, car_whl))


def convert_whl(whl):
    """Проверяет на корректность длину, ширину и высоту"""
    if whl == '':
        return "0x0x0"

    whl_splitted = whl.split("x")

    if len(whl_splitted) != 3:
        return "0x0x0"

    try:
        converted_whl = str(float(whl_splitted[0])) + "x" + str(
            float(whl_splitted[1])) + "x" + str(float(whl_splitted[2]))
        return converted_whl
    except ValueError:
        print("Неверный формат данных: {}". format(whl))
    else:
        return False


def create_spec_machine(row, car_list):
    """Создаёт объект класса Spec Machine"""
    try:
        car_type = row[0]
        car_brand = row[1]
        car_photo = row[3]
        car_carrying = float(row[5])
        car_extra = row[6]
    except ValueError:
        print("Неверный формат данных, пропускаю: {}".format(car_brand))
    else:
        return car_list.append(Truck(car_type, car_brand, car_photo, car_carrying, car_extra))


def get_car_list(csv_filename):
    """Обрабатывает входящий csv-файл"""
    car_list = []
    if os.path.exists(csv_filename) and os.path.getsize(csv_filename) > 0:
        with open(csv_filename) as csv_fd:
            reader = csv.reader(csv_fd, delimiter=';')
            next(reader)  # пропускаем заголовок
            for row in reader:
                if len(row) != 7:
                    continue
                # if list(os.path.splitext(row[3]))[1] == '':
                #     continue
                else:
                    if row[0] == 'car':
                        create_car(row, car_list)
                    if row[0] == 'truck' and convert_whl(row[4]):
                        create_truck(row, car_list)
                    if row[0] == 'spec_machine':
                        create_spec_machine(row, car_list)
    return car_list


print(str)

for i in get_car_list("coursera_week3_cars.csv"):
    print(vars(i))
    print("File ext: {}". format(i.get_photo_file_ext))
    if i.car_type == 'truck':
        print("Volume: {}".format(i.get_body_volume))
