import sys
import numpy as np


def main():
    k = int(input())
    scalars = np.array(list(map(float, input().split())))
    vectors = np.array([list(map(float, input().split())) for _ in range(k)])
    
    lin_comb = scalars @ vectors
    
    print(*lin_comb.round(2), sep=' ')
    

if __name__ == '__main__':
    main()