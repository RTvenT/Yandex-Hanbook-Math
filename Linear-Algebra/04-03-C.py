import sys
import numpy as np


def main():
    n = int(input())
    A = np.array([list(map(int, input().split())) for _ in range(n)])
    
    res = A
    k = 1
    
    while not np.all(res == 0):
        res = np.dot(res, A)
        k += 1
        
    print(k)
    
    
if __name__ == '__main__':
    main()