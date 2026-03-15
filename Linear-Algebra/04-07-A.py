import sys 
import numpy as np


def main():
    k = int(input())
    vecs = np.array([list(map(float, input().split())) for _ in range(k)])
    
    L1_norm = np.abs(vecs).sum(axis=1).round(4)

    print(*L1_norm, sep='\n')
    
    
if __name__ == '__main__':
    main()