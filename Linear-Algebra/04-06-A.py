import sys
import numpy as np


def adj(A):
    n = A.shape[0]
    adj_mat = np.zeros(shape=A.shape)
    indices = np.arange(n)
    
    for i in range(n):
        for j in range(n):
            adj_mat[i, j] = (-1)**(i+j) * np.linalg.det(A[np.ix_(indices != i, indices != j)])
            
    return adj_mat.T


def main():
    n = int(input())
    A = np.array([list(map(int, input().split())) for _ in range(n)])
    
    A_inv = (adj(A) / np.linalg.det(A)).round().astype(int)
    
    for row in A_inv:
        print(*row, sep=' ')
        
    
if __name__ == '__main__':
    main()