# Создайте родительский(базовый) класс Vehicle, который имеет свойство vehicle_type = "none"
# Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers, которая возвращает количество
# лошидиных сил для автомобиля
# Создайте наследника класса Car и Vehicle - класс Nissan и переопределите свойство price и vehicle_type, а также переопределите функцию horse_powers
# Создайте экзмепляр класса Nissan и распечайте через функцию print vehicle_type, price

class Vehicle:
    def __init__(self,vehicle_type = None):
        self.vehicle_type = vehicle_type

class Car:
    def __init__(self, horse_power, price=1000000):
        self.price = price
        self.horse_power = horse_power

    def horse_powers(self):
        return self.horse_power

class Nissan(Vehicle,Car):
    def __init__(self,price,vehicle_type,horse_power):
        Vehicle.__init__(self,vehicle_type)
        Car.__init__(self,price,horse_power)

    def horse_powers(self):
        print(self.horse_power)
car1 = Nissan(900000,"car",120)

print(car1.vehicle_type)
print(car1.price)
