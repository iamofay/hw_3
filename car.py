from abc import ABC
import exceptions


class Vehicle(ABC):
    w = 100
    s = 'not-started'
    f = 80
    fc = 10

    def __init__(self, weight=w, fuel=f, fuel_consumption=fc, started=s):
        self.weight = weight
        self.started = started
        self.fuel_consumption = fuel_consumption
        self.fuel = fuel

    def start(self):
        try:
            if self.started != 'started' and self.fuel > 0:
                self.started = 'started'
                return self.started
            else:
                raise exceptions.LowFuelError(f'Не достаточно топлива')
        except exceptions.LowFuelError as lfe:
            return lfe

    def move(self):
        try:
            if (self.fuel / self.fuel_consumption - self.weight) < 0:
                raise exceptions.NotEnoughFuel(
                    f'Не достаточно топлива для преодоления расстояния\n'
                    )
            else:
                self.fuel = self.fuel / self.fuel_consumption - self.weight
                a = f'Оставшееся топливо:{self.fuel}\n'
                return a
        except exceptions.NotEnoughFuel as nefe:
            return nefe

    def __str__(self):
        return (
            f'Расстояние для преодоления: {self.weight}\n'
            f'Расход топлива: {self.fuel_consumption}\n'
            f'Общее количество топлива: {self.fuel}\n'
        )


class Car(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, started='not-started'):
        super().__init__(weight, fuel, fuel_consumption, started)
        self.engine = None

    def set_engine(self, eng):
        self.engine = eng.volume, eng.pistons

    def __str__(self):
        return (
            f'Расстояние для преодоления: {self.weight}\n'
            f'Расход топлива: {self.fuel_consumption}\n'
            f'Общее количество топлива: {self.fuel}\n'
            f'Двигатель (объем,количество цилиндров): {self.engine}\n'
        )
