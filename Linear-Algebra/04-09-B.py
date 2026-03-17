import sys
import numpy as np


def main():
    n = int(input())
    A = np.array([list(map(float, input().split())) for _ in range(n)])
    b = np.array(list(map(float, input().split())))
    
    if not np.allclose(A, A.T) or np.any(np.linalg.eigvals(A) <= 0):
        print('FAIL')
        print('nan')
        return 0
    
    L = np.linalg.cholesky(A)
    y = np.linalg.solve(L, b)
    x = np.linalg.solve(L.T, y).round(4)
    r = np.linalg.norm(A @ x.T - b).round(4)
    
    print(*x, sep=' ')
    print(r)
    
    
    
if __name__ == '__main__':
    main()
    
    