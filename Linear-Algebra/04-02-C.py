import sys
import numpy as np


def main():
    A = np.array([list(map(int, input().split())) for _ in range(2)]).T
    v3 = np.array(list(map(int, input().split())))
    
    if abs(np.linalg.det(A)) < 1e-9:
        print('NO_SOLUTION')
        return 0
    
    lam = np.linalg.solve(A, v3)
    
    if not np.allclose(lam, np.round(lam)):
        print('NO_SOLUTION')
        return 0
    
    print(*lam.astype(int), sep=' ')
    
    
if __name__ == '__main__':
    main()