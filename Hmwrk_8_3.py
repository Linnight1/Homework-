class Car:
    def __init__(self, model,vin,numbers):
        self.model = model
        if Car.__is_valid_vin(self,vin) == True:
            self.__vin = vin
        if Car._is_valid_numbers(self,numbers) == True:
            self.__numbers = numbers

    def __is_valid_vin(self,vin):
        self.vin_number = vin
        if isinstance(self.vin_number, int) != True:
            raise IncorrectVinNumbers ("Некорректный тип vin номер")
        if self.vin_number not in range(1000000,10000000):
            raise IncorrectVinNumber ("Неверный диапазон для vin номера")
        else:
            return True

    def _is_valid_numbers(self,numbers):
        self.numbers = numbers

        if isinstance(self.numbers, str) != True:
            raise IncorrectCarNumbers ("Некорректный тип данных для номеров")
        if len(self.numbers) != 6:
            raise IncorrectCarNumbers ("Неверная длина номера")
        else:
            return True

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class  IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')


