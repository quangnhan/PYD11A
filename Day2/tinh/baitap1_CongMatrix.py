matrix1 = [
    [2, 3, 4],
    [2, 5, 5],
    [4, 5, 8]
]

matrix2 = [
    [4, 4, 5],
    [5, 6, 6],
    [5, 4, 6]
]

matrix = []
for i in range(len(matrix1)):
    temp = []
    for j in range(len(matrix1[i])):
        temp.append(matrix1[i][j] + matrix2[i][j])
    matrix.append(temp)
print(matrix)