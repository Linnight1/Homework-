# Дан список, состоящий из 50 элементов, определить сколько из них кратны 41 и больше среднего
# арифметического наибольшего и наименьшего значений списка. Для поиска максимального и минимальных
# значений использовать сортировку и индексы

import random
a = []
while len(a) < 50:
    a.append(random.randrange(1,100000))
c = sorted(a)[0] + sorted(a)[-1]
count = 0
for i in a:
    if i % 41 == 0 and i > c / 2:

        count += 1
print(count)

# import random
# a = []
# while len(a) < 50:
#     a.append(random.randrange(1,100000))
#
# count = 0
# for i in a:
#     if i % 41 == 0 and i > sum(sorted(a)[0],sorted(a)[-1]) / 2:
#
#         count += 1
# print(count)