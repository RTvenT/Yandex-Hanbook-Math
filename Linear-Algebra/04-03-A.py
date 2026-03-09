import sys
import numpy as np


def main():
    n = int(input())
    A = np.array([list(map(float, input().split())) for _ in range(n)])
    
    res = 'OTHER'
    
    A1 = A.copy()
    np.fill_diagonal(A1, 0)
    
    if np.all(A1 == 0):
        res = 'DIAGONAL'
    elif np.all(np.tril(A) == A):
        res = 'LOWER_TRIANGULAR'
    elif np.all(np.triu(A) == A):
        res = 'UPPER_TRIANGULAR'
        
    print(res)
        
        
if __name__ == '__main__':
    main()