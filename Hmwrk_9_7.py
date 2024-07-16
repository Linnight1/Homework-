def is_prime(sum_three):
    def wrapper(*args,**kwargs):
        b = sum_three(*args,**kwargs)
        for i in list(range(2,b)):
            if b % i == 0:
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