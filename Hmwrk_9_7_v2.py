def is_prime(func):
    def wrapper(*args,**kwargs):
        b = func(*args)
        if 0 in map(lambda x: b % x,range(2,b)):
            res = "Составное"
            return res, b
        else:
            res = "Простое"
            return res, b
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)
result = sum_three(2, 3, 6)
print(result)