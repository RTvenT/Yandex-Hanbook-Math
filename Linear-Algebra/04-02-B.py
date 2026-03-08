import sys
import numpy as np


def main():
    n = int(input())
    
    v = np.array(list(map(int, input().split())))
    u = np.array(list(map(int, input().split())))
    
    res = 'NON-ORTHOGONAL'
    
    if np.dot(u, v) == 0:
        res = 'ORTHOGONAL'
        
    print(res)
    
    
if __name__ == '__main__':
    main()