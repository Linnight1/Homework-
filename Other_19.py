# Реализация простого калькулятора:
# Создайте функцию, которая принимает строку с простым арифметическим выражением (например, "2 + 3 * 4 - 5")
# и вычисляет его, учитывая приоритет операций.

string_= "2+3+2-2-4"
def func_(string_):
    string = list(string_)
    count = 0
    ind = 0
    lst = []



    if "*" or ":" or "*" and ":" not in string:
        for i in string:
            count += 1
            ind = count - 1
            if i == "+":
                middle_res = int(string[ind - 1]) + int(string[ind + 1])
                print(middle_res)
                string[string.index(string[ind - 1]):string.index((string[ind + 2]))] == str(middle_res)

            if i == "-":
                middle_res = int(string[ind - 1]) - int(string[ind + 1])
                print(middle_res)
                string[string.index(string[ind - 1]):string.index((string[ind + 2]))] = str(middle_res)

        print(string)



        # elif "*" or ":" in string:
        #     for i in string:
        #         count += 1
        #         i == "*" or i == ":":
        #         ind = r - 1
        #         if i == '*':
        #             middle_res = int(string[ind - 1]) * int(string[ind + 1])
        #             print(middle_res)
        #             string[string.index(string[ind - 1]):string.index((string[ind + 2]))] = str(middle_res)
        #             print(string)
        #             func_(string)
        #
        #
        #
        #         if i == ':':
        #             middle_res = int(string[ind - 1]) // int(string[ind + 1])
        #             string[string.index(string[ind - 1]):string.index((string[ind + 2]))] = str(middle_res)
        #             print(string)
        #             func_(string)



                # else:
                #     if string[ind + 2] == ":" or string[ind + 2] == "*":
                #         if string[ind] == '*':
                #             middle_res = int(string[ind - 1]) * int(string[ind + 1])
                #             print(middle_res)
                #
                #             string[string.index(string[ind - 1]):string.index((string[ind + 2]))] = str(middle_res)
                #             print(string)
                #             func_(string)
                #
                #
                #         if string[ind] == ':':
                #             middle_res = int(string[ind - 1]) // int(string[ind + 1])
                #             print(middle_res)
                #
                #             print(middle_res)
                #             string[string.index(string[ind - 1]):string.index((string[ind + 2]))] = str(middle_res)
                #             print(string)
                #             func_(string)








