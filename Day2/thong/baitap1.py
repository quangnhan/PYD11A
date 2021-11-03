matrix1 = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]

matrix2 = [[8, 9, 10], [11, 12, 13], [14, 15, 16]]

matrix3 = []

for i in range(len(matrix1)):
    temp = []
    for x in range(len(matrix1[i])):
        temp.append(matrix1[i][x] + matrix2[i][x])
    matrix3.append(temp)


print(matrix3)
