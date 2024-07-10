list_ = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
res = map(lambda x: x*x, filter(lambda x: x % 2,list_))
print(list(res))


def f1(x):
    return x % 2
def f2(x):
    return x * x
result = map(f2,filter(f1,list_))
print(list(result))