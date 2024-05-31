matrix = [[2, 6, 8], [7, 4, 1], [0, 8, 2]]

flat_matrix = []

for sub_matrix in matrix:
    for num in sub_matrix:
        flat_matrix.append(num)


print(flat_matrix)

# flat_matrix_2 = [num for sub_matrix in matrix for num in sub_matrix]
flat_matrix_2 = [num for sub_matrix in matrix for num in sub_matrix]
print(flat_matrix_2)
