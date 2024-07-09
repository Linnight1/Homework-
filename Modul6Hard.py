import math


class Figure:
    sides_count = 0
    def __init__(self, color, sides, filled=bool):

        self.__color = color
        self.filled = filled
        if type (sides) != int:
            if Figure.__is_valid_sides(self, *sides) == True:
                self.__sides = sides
            else:
                self.__sides = 1
        else:
            self.__sides = sides
    def get_color(self):

        return self.__color

    def __is_valid_color(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b
        if self.r in range(1,256) and self.b in range(1,256) and self.b in range(1,256):
            return True
        else:
            return False

    def set_color(self,r,g,b):
        if Figure.__is_valid_color(self,r,g,b) == True:
            self.__color = [self.r,self.g,self.b]
            print("Цвет изменён")
        else:
            print("Цвет не изменён")

    def __is_valid_sides(self,*args):
        self.args = args

        for i in self.args:
            if type(i) == int and len(self.args) == self.sides_count:
                return True

            else:
                False

    def get_sides(self):
        side_list = []
        if type(self.__sides) == int:
            for i in range(1, self.sides_count + 1):
                side_list.append(self.__sides)
            return side_list
        else:
            for i in self.__sides:
                side_list.append(i)
            return side_list

    def __len__(self):
        return sum(Figure.get_sides(self))

    def set_sides(self, *new_sides):
        if Figure.__is_valid_sides(self,*new_sides) == True:
            self.__sides = new_sides
        else:
            print("Изменить не удалось")


class Circle(Figure):
    sides_count = 1
    def __init__(self, color, sides, filled = False):
        super().__init__(color, sides, filled)

    def __radius(self):

        return Circle.get_sides(self)[0] / ( math.pi * 2)

    def get_square(self):

        return math.pi * Circle.__radius(self) ** 2

class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, __sides, filled = False):
        super().__init__(__color, __sides, filled)


    def __height(self):
        p = Figure.__len__(self) / 2
        return (2 * math.sqrt(p  * (p - Triangle.get_sides(self)[0])*(p - Triangle.get_sides(self)[1])*(p -
                             Triangle.get_sides(self)[2]))) / Triangle.get_sides(self)[0]

    def get_square(self):
        return Triangle.get_sides(self)[0] * Triangle.__height(self) / 2

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides, filled = False):
        super().__init__(color, sides, filled)


    def get_volume(self):

        return Cube.get_sides(self)[0] ** 3




circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

c = Circle((200, 200, 100), (10, 15, 6))  # проверка на изменение сторон на неверное кол-во и создание взамен
                                                    # массива с нужным количеством сторон и значением один
print(c.get_sides())


tr = Triangle((12,14,145),(12,13,14))
print(tr.get_sides())


print(tr.get_square())
print(circle1.get_square())









