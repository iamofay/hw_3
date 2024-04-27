"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f"{self.text}"


class NotEnoughFuel(Exception):

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f"{self.text}"


class CargoOverload(Exception):

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f"{self.text}"
