import sys
import numpy as np


def main():
    n, d = map(int, input().split())
    
    X_train = np.array([list(map(float, input().split())) for _ in range(n)])
    alphas = np.array(list(map(float, input().split())))
    y_train = np.array(list(map(int, input().split())))
    gamma, b = map(float, input().split())
    t = int(input())
    X_test = np.array([list(map(float, input().split())) for _ in range(t)])
    K = lambda x, z: np.exp(-gamma * np.dot(x - z, x - z))
    
    for z in X_test:
        f = b
        for i in range(n):
            f += alphas[i] * y_train[i] * K(X_train[i], z) 
            
        y = 1 if f == 0 else int(np.sign(f))
        
        print(f, y)
        
        
if __name__ == '__main__':
    main()