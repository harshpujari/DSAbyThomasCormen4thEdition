#Strassen’s algorithm for matrix multiplication
#There are 2 more approaches for the same problme but not of much use, all are of O(n3)
def multiply(A, B, C):  
    for i in range(N):     
        for j in range( N):          
            C[i][j] = 0
            for k in range(N):            
                C[i][j] += A[i][k]*B[k][j]
