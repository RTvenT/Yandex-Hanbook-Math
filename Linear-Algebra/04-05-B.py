import sys
import numpy as np


def inv(A):
    n = A.shape[0]
    A_E = np.concatenate((A, np.eye(n)), axis=1)
    
    # forward
    for i in range(n):
        pivot_col = i
        pivot_elem = A_E[i, i]
        
        if np.allclose(pivot_elem, 0):
            return 'NON_INVERTIBLE'
        
        if i == n-1:
            break
        
        for j in range(i+1, n):
            pivot_under = A_E[j, pivot_col]
            
            if np.allclose(pivot_under, 0):
                continue
            
            A_E[j, :] *= pivot_elem
            A_E[j, :] -= pivot_under * A_E[i, :]
            
    # backward
    for i in range(n-1, -1, -1):
        pivot_col = i
        pivot_elem = A_E[i, i]
        
        if np.allclose(pivot_elem, 0):
            return 'NON_INVERTIBLE'
        
        if i == 0:
            break
        
        for j in range(i-1, -1, -1):
            pivot_over = A_E[j, pivot_col]
            
            if np.allclose(pivot_over, 0):
                continue
            
            A_E[j, :] *= pivot_elem
            A_E[j, :] -= pivot_over * A_E[i, :]
            
    # scaling
    for i in range(n):
        A_E[i:] /= A_E[i, i]
            
    return A_E[:, n:].round().astype(int)


def main():
    n = int(input())
    A = np.array([list(map(int, input().split())) for _ in range(n)])
    
    inv_A = inv(A)
    
    if not isinstance(inv_A, str):
        for row in inv_A:
            print(*row, sep=' ')
    else:
        print(inv_A)
    
    
if __name__ == '__main__':
    main()