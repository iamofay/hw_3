import engine
import car
import plane


def main():
    e1 = engine.Engine()
    v1 = car.Vehicle(200, 0, 8)
    print(f'Транспортное средство 1:\n{v1}')
    print(f'Статус: {v1.start()}\n')
    v2 = car.Vehicle(200, 10, 8)
    print(f'Транспортное средство 2:\n{v2}')
    print(f'Статус: {v2.start()}\n')
    v3 = car.Vehicle(200, 2000, 8)
    print(f'Транспортное средство 3:\n{v3}')
    print(v3.move())
    v4 = car.Vehicle(200, 200, 8)
    print(f'Транспортное средство 4:\n{v4}')
    print(v4.move())
    c1 = car.Car(200, 20000, 9)
    c1.start()
    c1.set_engine(e1)
    print(f'Автомобиль 1:\n{c1}')
    p1 = plane.Plane(200, 20000, 200, 200, 8)
    print(f'Самолет 1:\n{p1}')
    print(p1.load_cargo(2000))
    p2 = plane.Plane(200, 20000, 200, 200, 8)
    print(f'Самолет 2:\n{p2}')
    print(p2.load_cargo(20000))


main()
