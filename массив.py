s = sum([i for i in range(1, 100) if i % 2 == 0])
print(s)

def transpose_matrix(matrix):
    transposed = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed[j][i] = matrix[i][j]
    
    return transposed, sum([sum(i) for i in transposed])

print(transpose_matrix([[1,2,3], [4,5,6]]))

