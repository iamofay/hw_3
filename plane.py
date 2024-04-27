import car
import exceptions


class Plane(car.Vehicle):
    w = 100
    s = 'not-started'
    f = 80
    fc = 10

    def __init__(self, cargo, cargo_max, weight=w, fuel=f, fuel_consumption=fc, started=s):
        super().__init__(self, weight, fuel, fuel_consumption)
        self.started = started
        self.fuel_consumption = fuel_consumption
        self.fuel = fuel
        self.weight = weight
        self.cargo = cargo
        self.cargo_max = cargo_max

    def load_cargo(self, w):
        try:
            if (self.cargo + w) > self.cargo_max:
                raise exceptions.CargoOverload(
                    f'Перегрузка!:\n'
                    f'Предполагаемый вес больше максимального на: {self.cargo + w - self.cargo_max}\n'
                )
            else:
                self.cargo = self.cargo + w
            return f'Вес с грузом: {self.cargo}\n'
        except exceptions.CargoOverload as col:
            return col

    def remove_all_cargo(self):
        carg = self.cargo
        self.cargo = 0
        return carg

    def __str__(self):
        return (
            f'Расстояние для преодоления: {self.weight}\n'
            f'Статус: {self.started}\n'
            f'Расход топлива: {self.fuel_consumption}\n'
            f'Общее количество топлива: {self.fuel}\n'
            f'Вес самолета: {self.cargo}\n'
            f'Максимальная грузоподъемность: {self.cargo_max}\n'
        )
