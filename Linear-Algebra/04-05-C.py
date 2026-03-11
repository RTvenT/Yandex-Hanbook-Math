import sys
import numpy as np


def lu(A):
    n = A.shape[0]
    U = A.copy()
    L = np.eye(n)
    
    # forward
    for i in range(n):
        pivot_col = i
        pivot_elem = U[i, i]
        
        if np.allclose(pivot_elem, 0):
            return 'FAIL'
        
        if i == n-1:
            break
        
        for j in range(i+1, n):
            pivot_under = U[j, pivot_col]
            
            if np.allclose(pivot_under, 0):
                continue
            
            l_ji = pivot_under / pivot_elem
            
            U[j, :] -= l_ji * U[i, :]
            L[j, i] = l_ji
            
            
    return np.array([L, U]).round().astype(int)


def main():
    n = int(input())
    A = np.array([list(map(float, input().split())) for _ in range(n)])
    
    LU = lu(A)
    
    if not isinstance(LU, str):
        for row in LU[0]:
            print(*row, sep=' ')
        for row in LU[1]:
                print(*row, sep=' ')
    else:
        print(LU)    
    
if __name__ == '__main__':
    main()
    