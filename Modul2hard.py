num = int(input("Какой число выпало? Введите для полученися пароля: \n"))

list_ = [i for i in range(1,num)]
new_list = []
def password_for_save_your_life_maker(num):
    for i in list_:
        for r in list_:
            if num % (i+r) == 0:
                new_list.append([r,i])

    for i in new_list:
        i.sort()

    # new_list_2 = [i for i in new_list if i not in new_list_2]  Почему не получается?( Как это записать через list.comp ?
    new_list_2 = []
    for i in new_list:
        while i not in new_list_2 and i[0] != i[1]:
            new_list_2.append(i)
        else:
            continue

    return new_list_2


print(password_for_save_your_life_maker(num))










