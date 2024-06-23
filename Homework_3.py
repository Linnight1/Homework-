# Создайте родительский(базовый) класс Vehicle, который имеет свойство vehicle_type = "none"
# Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers, которая возвращает количество
# лошидиных сил для автомобиля
# Создайте наследника класса Car и Vehicle - класс Nissan и переопределите свойство price и vehicle_type, а также переопределите функцию horse_powers
# Создайте экзмепляр класса Nissan и распечайте через функцию print vehicle_type, price

class Vehicle:
    def __init__(self,vehicle_type,price,horse_power):
        self.vehicle_type = vehicle_type
        self.vehicle_type = None
        super().__init__(price,horse_power)
class Car:
    def __init__(self,price,horse_power):
        self.price = price
        self.price = 1000000
        self.horse_power = horse_power

    def horse_powers(self):
        return self.horse_power
class Nissan(Vehicle,Car):
    def __init__(self,vehicle_type,price,horse_power):
        super().__init__(vehicle_type,price,horse_power)
        self.vehicle_type = "car"
        self.price = 900000
        super().horse_powers()
car1 = Nissan(1,2,3)

print(car1.vehicle_type)
print(car1.price)
