matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix2 = [
    [1,2,1],
    [2,2,3],
    [1,4,3]
]

matrix3 = []

for i in range(len(matrix1)):
    temp = []
    for j in range(len(matrix1[i])):
        temp.append(matrix1[i][j] + matrix2[i][j])
    matrix3.append(temp)

print(matrix3)