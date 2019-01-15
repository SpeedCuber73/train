import os
import csv
import sys

car_type = ["car", "truck", "spec_machine"]
car = 0
truck = 1
spec_machine = 2


class WrongFormatError(Exception):

    def __init__(self, message):
        self.message = message


class CarBase:
    idx_car_type = 0
    idx_brand = 1
    idx_passenger_seats_count = 2
    idx_photo_file_name = 3
    idx_body_whl = 4
    idx_carrying = 5
    idx_extra = 6

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = car_type[car]
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = car_type[truck]
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
        self.car_type = car_type[spec_machine]
        self.extra = extra


def get_vehicle(params):
    try:
        if params[CarBase.idx_car_type] == car_type[car]:
            return Car(
                params[CarBase.idx_brand],
                params[CarBase.idx_photo_file_name],
                float(params[CarBase.idx_carrying]),
                int(params[CarBase.idx_passenger_seats_count])
            )
        if params[CarBase.idx_car_type] == car_type[truck]:
            return Truck(
                params[CarBase.idx_brand],
                params[CarBase.idx_photo_file_name],
                float(params[CarBase.idx_carrying]),
                params[CarBase.idx_body_whl]
            )
        if params[CarBase.idx_car_type] == car_type[spec_machine]:
            return SpecMachine(
                params[CarBase.idx_brand],
                params[CarBase.idx_photo_file_name],
                float(params[CarBase.idx_carrying]),
                params[CarBase.idx_extra]
            )
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
