import sys
import numpy as np



def solve(A, b):
    A_b = np.concatenate((A, b[:, np.newaxis]), axis=1)
    n = A.shape[0]
    
    # forward
    for i in range(n):
        if np.allclose(A_b[:, i], 0):
            return 'NO_SINGLE_SOLUTION'
        
        if i == n-1:
            break
        
        pivot_row_idx = A_b[i:,i].argmax() + i
        A_b[[i, pivot_row_idx]] = A_b[[pivot_row_idx, i]]
        pivot_elem = A_b[i, i]
        
    
        for j in range(i+1, n):
            pivot_under = A_b[j, i]
            
            if np.allclose(pivot_under, 0):
                continue
            
            A_b[j, :] *= pivot_elem
            A_b[j, :] -= pivot_under * A_b[i, :]
            
            
    # backward
    for i in range(n-1, -1, -1):
        if np.allclose(A_b[:, i], 0):
            return 'NO_SINGLE_SOLUTION'
        
        if i == 0:
            break
       
        pivot_elem = A_b[i, i]
        
        for j in range(i-1, -1, -1):
            pivot_over = A_b[j, i]
            
            if np.allclose(pivot_over, 0):
                continue
            
            A_b[j, :] *= pivot_elem
            A_b[j, :] -= pivot_over * A_b[i, :]
            
            
    # solution
    x = np.zeros(n)
    
    for i in range(n):
        x[i] = A_b[i, -1] / A_b[i, i]
            
    return x.round().astype(int)
            

def main():
    n = int(input())
    A = np.array([list(map(int, input().split())) for _ in range(n)])
    b = np.array(list(map(int, input().split())))
    
    x = solve(A, b)
    
    if isinstance(x, str): 
        print(x)
    else:
        print(*x, sep=' ')
    
    
if __name__ == '__main__':
    main()