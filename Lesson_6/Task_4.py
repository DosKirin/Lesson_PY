# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Марка машины {self.name} едет'

    def stop(self):
        return f'\nМарка машины {self.name} будет остановленна '

    def turned(self,direction):
        return f'\nМарка машины {self.name} повернет {direction}'

    def show_speed(self):
        return  f'\nСкорость машины {self.name}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nСкорость превышает допустимый предел {self.speed}'
        else:
            return f'\nСкорость {self.name} в норме'


class Sportcar(Car):
    pass

class WorkСar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nСкорость превышает допустимый предел {self.speed}'
        else:
            return f'\nСкорость машины {self.name} в норме'


class PoliceCar(Car):
    pass



town = TownCar(90, 'Серый', 'Tesla_Model_X', False)
print('1:\n' + town.go(), town.show_speed(), town.turned('налево'), town.stop())

sport = Sportcar(60, 'Белый', 'Nissan_Patrol',  False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turned('не поворачивает'), sport.stop())

work = WorkСar(int(input('Введите скорость 3й машины:')), 'Невидимая', 'patriot',  False)
print('3:\n' + work.go(), work.show_speed(), work.turned('направо'), work.stop())

police = PoliceCar (int(input('Введите скорость 4й машины:')), 'Вишневая', 'priora', True)
print('4:\n' + police.go(), police.show_speed(), police.turned('без поворота'), police.stop())




