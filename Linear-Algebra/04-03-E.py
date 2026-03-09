import sys
import numpy as np


def main():
    m, n = map(int, input().split())
    A = np.array([list(map(int, input().split())) for _ in range(m)])
    
    A_normed = ((A - np.mean(A, axis=0)) / np.std(A, axis=0)).astype(int)
    
    for row in A_normed:
        print(*row, sep=' ')
        
        
if __name__ == '__main__':  
    main()