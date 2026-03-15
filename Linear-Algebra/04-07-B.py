import sys
import numpy as np 


def main():
    k = int(input())
    vecs = np.array([list(map(float, input().split())) for _ in range(k)])
    
    L2_norm = np.sqrt((vecs**2).sum(axis=1))
    
    print(*L2_norm, sep='\n')
    
    
if __name__ == '__main__':
    main()