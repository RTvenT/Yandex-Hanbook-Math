import sys
import numpy as np 


def main():
    k = int(input())
    vecs = np.array([list(map(float, input().split())) for _ in range(k)])
    
    L_inf_norm = np.max(np.abs(vecs), axis=1).round(4)
    
    print(*L_inf_norm, sep='\n')
    
    
if __name__ == '__main__':
    main()