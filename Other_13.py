
def func(some_str,list_):

    for i in list_:
        a = i[0]
        b = i[1]
        c = i[2]
        print(a,b,c)
        return funcOfRom(some_str,a,b,c,list_)


def funcOfRom(some_str,a,b,c,list_):
    print(some_str,a,b,c)

    print(some_str[-1])
    num = int(some_str[-1])
    if num < 4:
        res = a * num
        print(res)
    elif num == 4:
        res = a + b
        print(res)
    elif num >= 5 and num < 9:
        x = a * (num - 5)
        res = b + x
        print(res)
    elif num == 9:
        res = a + c
    some_str = res + some_str[0:-1]
    print(some_str)
    list_.pop(0)


    if some_str.isalpha() == False:

        return func(some_str,list_)
    else:
        return some_str

list_ = [["I","V","X"],["X","L","C"],["C","D","M"],["M","V","X"],["X","L","C"],["C","D","M"]]
string = "683"
print(func(string,list_))
















