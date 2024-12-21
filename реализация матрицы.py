def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Количество столбцов в первой матрице должно совпадать с количеством строк во второй.")
    
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    
    return result


def mean_squared_error(actual, predicted):
    if len(actual) != len(predicted):
        raise ValueError("Длины списков должны совпадать.")
        
    mse = sum((a - p) ** 2 for a, p in zip(actual, predicted)) / len(actual)
    return mse

print(matrix_multiply([[1,2,3], [2,3,4], [4,5,7]], [[14,52,63], [12,23,42], [42,52,72]]))

print(mean_squared_error([1,2,3], [5,5,5]))