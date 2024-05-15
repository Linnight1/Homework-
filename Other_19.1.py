def func_(i, a, b):
    if i == "*":
        return float(a) * float(b)
    if i == ":":
        return float(a) / float(b)
    if i == "+":
        return float(a) + float(b)
    if i == "-":
        return float(a) - float(b)

def func_2(string):
    for i in string:
        if i == "*" or i == ":":
            string[string.index(i) + 1] = str(func_(i,string[string.index(i)-1],string[string.index(i)+1]))
            string.pop(string.index(i) - 1)
            string.pop(string.index(i))
            func_2(string)
            func_3(string)
        elif "*" or ":" or "*" and ":" not in string:
            func_3(string)

def func_3(string):
    for i in string:
        if i == "+" or i == "-":
            string[string.index(i) + 1] = str(func_(i, string[string.index(i) - 1], string[string.index(i) + 1]))
            string.pop(string.index(i) - 1)
            string.pop(string.index(i))
            if len (string) >= 3:
                func_3(string)
            else:
                print(string)

string = list(input("Введите пример:\n"))

func_2(string)

















