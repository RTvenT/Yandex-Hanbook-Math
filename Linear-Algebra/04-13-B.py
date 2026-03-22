import sys
import numpy as np


def main():
    m, n = map(int, input().split())
    X = np.array([list(map(float, input().split())) for _ in range(m)])
    eps = float(input())
    gamma = np.array(list(map(float, input().split())))
    beta = np.array(list(map(float, input().split())))
    
    mean = X.mean(axis=0, keepdims=True)
    var = X.var(axis=0, keepdims=True)
    
    X_normed = (X - mean) / np.sqrt(var + eps)
    Y = gamma * X_normed + beta
    
    for y in Y:
        print(*y, sep=' ')
        
    print(*mean[0].round(4), sep=' ')
    print(*var[0].round(4), sep=' ')
    
    
if __name__ == '__main__':
    main()
    
    