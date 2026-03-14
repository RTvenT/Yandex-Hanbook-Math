import sys 
import numpy as np


def main():
    n = int(input())
    x = np.array(list(map(int, input().split())))
    
    vander_det = 1
    
    for i in range(n):
        for j in range(i + 1, n):
            vander_det *= (x[j] - x[i])
            
    print(vander_det)
    
    
if __name__ == '__main__':
    main()