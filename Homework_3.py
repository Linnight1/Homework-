def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params()
print_params(a=2,b=["a","b","c"])
print_params(b= 565)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [ 4, "some_string", False]
values_dict = {"a": 1, "b": "some_string", "c": False}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [565, (9,8,7)]
print_params(*values_list_2, 42)