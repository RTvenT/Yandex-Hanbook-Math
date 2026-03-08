import sys
import numpy as np


def main():
    m, n = map(int, input().split())
    
    A = np.array([list(map(int, input().split())) for _ in range(m)])
    rk = np.linalg.matrix_rank(A)
    
    if rk >= m:
        print('LINEARLY_INDEPENDENT')
    else:
        print('LINEARLY_DEPENDENT')
        
        
if __name__ == '__main__':
    main()
