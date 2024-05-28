# Слияние перекрывающихся интервалов:
# Дан список интервалов в виде
# кортежей(start, end).Напишите  функцию, которая  объединяет  все перекрывающиеся интервалы  в  один
# и возвращает  список неперекрывающихся интервалов.

#
list_1 = [(4,13),(1,4),(5,7)]
def func_(some_list):
    new_list = []
    list_of_set = []
    intersection_list = []
    new_list_2 = []
    a = 0
    b = 0

    for i in some_list:
        new_list.append([j for j in range(i[0],i[1] + 1)])
        print(new_list)
    for i in new_list:
        list_of_set.append(set(i))
        print(list_of_set)
        print(* list_of_set)


    intersection_list.append(list_of_set[0]&list_of_set[1])
    intersection_list.append((list_of_set[1]&list_of_set[2]))
    intersection_list.append((list_of_set[0] & list_of_set[2]))
    intersection_list = intersection_list[0].union(intersection_list[1]).union(intersection_list[2])
    print(intersection_list)
    for i in new_list:
        for j in intersection_list:
            if j in i:
                i.remove(j)
    for i in new_list:
        if len(i) > 1:
            new_list_2.append(min(i))
            new_list_2.append(max(i))
        else:
            pass

    return f"Перекрывающиеся инт-лы:{min(intersection_list), max(intersection_list),}неперекрывающиеся инт-лы:{ new_list_2}"

print(func_(list_1))




