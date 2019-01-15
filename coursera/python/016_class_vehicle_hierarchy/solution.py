import os
import csv
import sys


car_type = ["car", "truck", "spec_machine"]


class WrongFormatError(Exception):

    def __init__(self, message):
        self.message = message


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = car_type[0]
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = car_type[1]
        self.__set_body_whl(body_whl)

    def __set_body_whl(self, body_whl):
        if not body_whl:
            self.body_length = 0.0
            self.body_width = 0.0
            self.body_height = 0.0
        else:
            try:
                list_body_whl = body_whl.split('x')
                if len(list_body_whl) != 3:
                    raise WrongFormatError("Error! parameter body_whl don's consist of three parts")
                self.body_length = float(list_body_whl[0])
                self.body_width = float(list_body_whl[1])
                self.body_height = float(list_body_whl[2])
            except ValueError:
                raise WrongFormatError("Error! Can't parse parameter body_whl")

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = car_type[2]
        self.extra = extra


def get_vehicle(params):
    try:
        if params[0] == car_type[0]:
            return Car(params[1], params[3], float(params[5]), int(params[2]))
        if params[0] == car_type[1]:
            return Truck(params[1], params[3], float(params[5]), params[4])
        if params[0] == car_type[2]:
            return SpecMachine(params[1], params[3], float(params[5]), params[6])
        else:
            return None
    except IndexError:
        return None
    except ValueError:
        return None
    except WrongFormatError:
        return None


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename, 'r') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            vehicle = get_vehicle(row)
            if vehicle:
                car_list.append(vehicle)
    return car_list


if __name__ == "__main__":
    print(get_car_list(sys.argv[1]))
