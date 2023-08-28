#Strassen’s algorithm for matrix multiplication
#There are 2 more approaches for the same problme but not of much use, all are of O(n3)

def square_matrix_multiply(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C

# Example usage
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = square_matrix_multiply(A, B)

for row in result:
    print(row)

