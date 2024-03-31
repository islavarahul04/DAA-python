import time

def matrix_multiply(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return "Matrices cannot be multiplied: Invalid dimensions"
    
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

def calculate_time_complexity(matrix1, matrix2):
    start_time = time.time()
    result = matrix_multiply(matrix1, matrix2)
    end_time = time.time()
    
    time_taken = end_time - start_time
    print("Time taken for matrix multiplication: {:.6f} seconds".format(time_taken))

# Example usage:
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

calculate_time_complexity(matrix1, matrix2)
