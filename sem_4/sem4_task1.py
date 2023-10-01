# Напишите функцию для транспонирования матрицы

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]



matrix1 = [[2, 3],
          [4, 5]]
print(transpose(matrix1)) # [[2, 4], [3, 5]]

matrix2 = [[2, 6],
           [3, 7],
           [4, 8],
           [5, 9]]
print(transpose(matrix2)) # [[2, 3, 4, 5], [6, 7, 8, 9]]

matrix3 = [[2, 6, 11],
           [3, 7, 12],
           [4, 8, 13],
           [5, 9, 14]]
print(transpose(matrix3)) # [[2, 3, 4, 5], [6, 7, 8, 9], [11, 12, 13, 14]]

