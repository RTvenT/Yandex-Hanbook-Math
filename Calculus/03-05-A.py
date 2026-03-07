import sys
import numpy as np
from numpy import linalg as LA 


def main():
    eps = 1e-12
    
    Hessian = np.array([list(map(float, row.split())) for row in sys.stdin])
    b = np.sum(Hessian[[0, 1], [1, 0]]) / 2
    Hessian[0, 1] = b
    Hessian[1, 0] = b
    
    eigen_values = LA.eigvals(Hessian)
    
    res = 'SADDLE'
    
    if np.any(np.abs(eigen_values) <= eps):
        res = 'UNKNOWN'
    elif np.all(eigen_values > 0):
        res = 'MIN'
    elif np.all(eigen_values < 0):
        res = 'MAX'
        
    print(res)
    
    

if __name__ == '__main__':
    main()

