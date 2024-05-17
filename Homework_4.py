def test_func(*params):
    print(params)
test_func(1,2,3,4,5,6,7)
def func_1(n):
    if n == 0:
        return 1
    else:
        return n * func_1 (n - 1)



print(func_1(5))