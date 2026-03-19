import sys
import numpy as np


def main():
    m, n = map(int, input().split())
    A = np.array([list(map(float, input().split())) for _ in range(m)])
    r = A.mean(axis=0, keepdims=True).round(4)
    Z = (A - r).round(4)
    
    for row in Z:
        print(*row, sep=' ')
        
    print(*r[0,:], sep=' ')
    
    
if __name__ == '__main__':
    main()