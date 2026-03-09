import sys
import numpy as np


def transpose(A):
    m, n = A.shape
    A_t = []
    
    for j in range(n):
        A_t.append(A[:, j])
        
    return np.array(A_t)


def main():
    m, n = map(int, input().split())
    A = np.array([list(map(int, input().split())) for _ in range(m)])
    A_t = transpose(A)
    
    for row in A_t:
        print(*row, sep=' ')
        
        
if __name__ == '__main__':
    main()