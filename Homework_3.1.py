# Создайте новый класс Building
# Создайте инициализатор для класса Building, который будет задавать целочисленный атрибут этажности self.numberOfFloors
# и строковый атрибут self.buildingType
# Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения

class Building():
    def __init__(self,numberOfFloors,buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType
    def __eq__(self, other):
        return self.buildingType == other.buildingType and self.numberOfFloors == other.numberOfFloors
h1 = Building(25, "Высотное здание")
h2 = Building (10,"Жилой дом")
h3 = Building(25,"Многоэтажка")
h4 = Building(25,"Высотное здание")
print(h1 == h2)
print(h2 == h3)
print(h1 == h4)