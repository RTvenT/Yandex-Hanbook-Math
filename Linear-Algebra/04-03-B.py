import sys
import numpy as np


def dot(A, B):
    m, n = A.shape
    k = B.shape[1]
    C = np.zeros(shape=(m, k))
    
    for i in range(m):
        for j in range(k):
            C[i][j] = np.dot(A[i, :], B[:, j])
            
    return C.astype(int)


def main():
    m, n = map(int, input().split())
    A = np.array([list(map(int, input().split())) for _ in range(m)])
    
    h, k = map(int, input().split())
    B = np.array([list(map(int, input().split())) for _ in range(h)])
    
    if h != n:
        print('NOT_DEFINED')
        return 0
    
    C = dot(A, B)
    
    for row in C:
        print(*row, sep=' ')
        
    
if __name__ == '__main__':
    main()