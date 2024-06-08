# Дана матрица (список списков) целых чисел.
# Напишите функцию, которая транспонирует матрицу (меняет строки на столбцы) и возвращает новую матрицу.
# import numpy as np
# listOfLists = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = np.listOfLists
# matrix_transpose = matrix.transpose()
# print(matrix_transpose)
listOfLists = [[1,2,3],[4,5,6],[7,8,9]]
listOfLists_2 = [[] for i in range(len(listOfLists))]

lenOfListOfLists = [i for i in range (0, len(listOfLists))]
def matrix_func_(listOfLists,lenOfListOfLists):
    if len(listOfLists[0]) > 0:
        for i in listOfLists:
            listOfLists_2[lenOfListOfLists[0]].append(i[0])

        for i in listOfLists:
            i.pop(0)
        lenOfListOfLists.pop(0)


        matrix_func_(listOfLists,lenOfListOfLists)

        return listOfLists_2

    else:
        return 0


print(matrix_func_(listOfLists,lenOfListOfLists))
