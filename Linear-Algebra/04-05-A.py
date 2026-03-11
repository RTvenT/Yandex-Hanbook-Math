import sys
import numpy as np


def check_invertibility(A):
    n = A.shape[0]
    A_b = np.concatenate((A, np.eye(n)), axis=1)
    
    # forward
    for i in range(n):
        pivot_col = i
        pivot_elem = A_b[i, i]
        
        if np.allclose(pivot_elem, 0):
            return 'NON_INVERTIBLE'
        
        if i == n-1:
            break
        
        for j in range(i+1, n):
            pivot_under = A_b[j, pivot_col]
            
            if np.allclose(pivot_under, 0):
                continue
            
            A_b[j, :] *= pivot_elem
            A_b[j, :] -= pivot_under * A_b[i, :]
            
    # backward
    for i in range(n-1, -1, -1):
        pivot_col = i
        pivot_elem = A_b[i, i]
        
        if np.allclose(pivot_elem, 0):
            return 'NON_INVERTIBLE'
        
        if i == 0:
            break
        
        for j in range(i-1, -1, -1):
            pivot_over = A_b[j, pivot_col]
            
            if np.allclose(pivot_over, 0):
                continue
            
            A_b[j, :] *= pivot_elem
            A_b[j, :] -= pivot_over * A_b[i, :]
            
    return 'INVERTIBLE'


def main():
    n = int(input())
    A = np.array([list(map(int, input().split())) for _ in range(n)])
    
    res = check_invertibility(A)
    
    print(res)
    
    
if __name__ == '__main__':
    main()