data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
some_list = []
for i in data_structure:
    if isinstance(i, dict) == False:
        for j in i:
            if isinstance(j, list) == False:
                some_list.append(j)
            else:
                for k in j:
                    for x in k:
                        for y in x:
                            if isinstance(y, tuple) == False:
                                some_list.append(y)
                            else:
                                for z in y:
                                    some_list.append(z)

    else:
        some_list.append(i)


def func_(*args):
    res = []
    str_list_ = []
    result = 0
    if len(res) == 1:
        return 0
    else:
        for i in args:
            if isinstance(i,int) == True:
                res.append(i)
                result = sum(res)

            if isinstance(i, dict) == True:
                str_list_ = [len(i) for i in [*(i.keys())]]
                res = [*(i.values()),result,*str_list_]
                result = func_(res)

            if isinstance(i,str) == True:
                res.append(len(i))
                func_(res)

    return result
print(func_(*some_list))


