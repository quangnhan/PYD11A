matrix1 = [
    [1, 2, 4],
    [3, 5, 5],
    [3, 4, 4]
]

matrix2 = [
    [1, 3, 4],
    [4, 5, 5],
    [3, 4, 5]
]

matrix = []

matrix = []
for i in range(len(matrix1)):
    temp = []
    for j in range(len(matrix1[i])):
        temp.append(matrix1[i][j] - matrix2[i][j])
    matrix.append(temp)
print(matrix)
