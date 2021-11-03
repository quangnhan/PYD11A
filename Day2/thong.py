matrix1 = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]

matrix2 = [[8, 9, 10], [11, 12, 13], [14, 15, 16]]

matrix1_list = []

for list in matrix1:
    for x in list:
        matrix1_list.append(x)
print(matrix1_list)

for list in matrix2:
    for x in list:
        matrix3 = [x + num for num in matrix1_list]
print(matrix3)
