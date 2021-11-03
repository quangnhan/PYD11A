matrix1 = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]

matrix2 = [["a", "b", "c"], ["a", "b", "c"], ["a", "b", "c"]]

for x in matrix1:
    new_matrix = [item + x for item in matrix2]

print(new_matrix)
