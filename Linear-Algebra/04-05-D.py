import sys
import numpy as np


def cholesky(A):
    n = A.shape[0]
    L = np.zeros(shape=(n, n))
    
    is_whole_root = lambda x: np.isclose(x, round(x))
    
    l11 = np.sqrt(A[0, 0])
    if not is_whole_root(l11): 
        return 'FAIL'
    
    L[0, 0] = l11
    
    for j in range(1, n):
        L[j, 0] = A[j, 0] / L[0, 0]
    
    for i in range(1, n):
        for j in range(1, i+1):
            if j == i: # Main diag
                # print(j, L[j, :j], sep='\n')
                l_jj_squared = A[j, j] - np.dot(L[j, :j], L[j, :j])
                if l_jj_squared < 0:
                    return 'FAIL'
                
                l_jj = np.sqrt(l_jj_squared)
                if not is_whole_root(l_jj):
                    return 'FAIL'
                
                L[j, j] = l_jj
            else: # Under diag
                L[i, j] = (A[i, j] - np.dot(L[i, :j], L[j, :j])) / L[j, j]
                
    return L.round().astype(int)
    


def main():
    n = int(input())
    A = np.array([list(map(int, input().split())) for _ in range(n)])
    
    L = cholesky(A)
    
    if isinstance(L, str):
        print(L)
    else:
        for row in L:
            print(*row, sep=' ')
            
    
if __name__ == '__main__':
    main()
    
    