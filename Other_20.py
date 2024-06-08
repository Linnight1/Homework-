# Выделение уникальных элементов в нескольких списках:
# Даны несколько списков. Напишите функцию, которая возвращает список элементов,
# которые встречаются только в одном из предоставленных списков.
a = [1,2,3,124]
b = [1,2,7,3,4,"r"]
c = [1,2,4,5]

def unic_elems(*args):
    new_list = []
    res_ = []
    for i in args:
        for j in i:
            new_list.append(j)

    for i in new_list:
        if new_list.count(i) == 1:
            res_.append(i)
    return res_

print(unic_elems(a,b,c))