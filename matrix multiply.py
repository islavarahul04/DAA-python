def split_matrix(matrix):
    """
    Splits a matrix into four submatrices.
    
    Parameters:
        matrix (list of lists): The matrix to split.
        
    Returns:
        tuple: Four submatrices: A11, A12, A21, A22.
    """
    n = len(matrix)
    mid = n // 2
    
    A11 = [row[:mid] for row in matrix[:mid]]
    A12 = [row[mid:] for row in matrix[:mid]]
    A21 = [row[:mid] for row in matrix[mid:]]
    A22 = [row[mid:] for row in matrix[mid:]]
    
    return A11, A12, A21, A22

def add_matrices(A, B):
    """
    Adds two matrices element-wise.
    
    Parameters:
        A (list of lists): The first matrix.
        B (list of lists): The second matrix.
        
    Returns:
        list of lists: The sum of the two matrices.
    """
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]

def subtract_matrices(A, B):
    """
    Subtracts one matrix from another element-wise.
    
    Parameters:
        A (list of lists): The first matrix.
        B (list of lists): The second matrix.
        
    Returns:
        list of lists: The result of subtracting B from A.
    """
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]

def strassen_matrix_multiply(A, B):
    """
    Performs matrix multiplication using Strassen's algorithm.
    
    Parameters:
        A (list of lists): The first matrix.
        B (list of lists): The second matrix.
        
    Returns:
        list of lists: The product of matrices A and B.
    """
    # Base case: If matrices are 1x1, perform simple multiplication
    if len(A) == 1:
        return [[A[0][0] * B[0][0]]]
    
    # Split matrices into submatrices
    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)
    
    # Recursive steps for Strassen's algorithm
    M1 = strassen_matrix_multiply(add_matrices(A11, A22), add_matrices(B11, B22))
    M2 = strassen_matrix_multiply(add_matrices(A21, A22), B11)
    M3 = strassen_matrix_multiply(A11, subtract_matrices(B12, B22))
    M4 = strassen_matrix_multiply(A22, subtract_matrices(B21, B11))
    M5 = strassen_matrix_multiply(add_matrices(A11, A12), B22)
    M6 = strassen_matrix_multiply(subtract_matrices(A21, A11), add_matrices(B11, B12))
    M7 = strassen_matrix_multiply(subtract_matrices(A12, A22), add_matrices(B21, B22))
    
    # Calculate submatrices of the result
    C11 = add_matrices(subtract_matrices(add_matrices(M1, M4), M5), M7)
    C12 = add_matrices(M3, M5)
    C21 = add_matrices(M2, M4)
    C22 = add_matrices(subtract_matrices(add_matrices(M1, M3), M2), M6)
    
    # Combine submatrices into the result matrix
    result = []
    for i in range(len(C11)):
        result.append(C11[i] + C12[i])
    for i in range(len(C21)):
        result.append(C21[i] + C22[i])
        
    return result

# Test the function
A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

B = [[17, 18, 19, 20],
     [21, 22, 23, 24],
     [25, 26, 27, 28],
     [29, 30, 31, 32]]

result = strassen_matrix_multiply(A, B)
print("Matrix A:")
for row in A:
    print(row)
print("\nMatrix B:")
for row in B:
    print(row)
print("\nResultant Matrix:")
for row in result:
    print(row)
