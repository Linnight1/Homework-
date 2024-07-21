from threading import  Thread
import time
class Knight(Thread):

    def __init__(self,name, power,enemies = 100):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = enemies


    def run(self):
        count = 0
        print(f"{self.name}, на нас напали! \n")
        for i in range(self.power + 1):
            count+=1
            print(f"{self.name} сражается {i} дня(дней), осталось {self.enemies} врагов. \n")
            time.sleep(1)
            self.enemies = self.enemies - self.power
            if self.enemies == 0:
                print(f"{self.name} одержал победу спустя {count} дней! \n")
                break



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все враги повержены")









