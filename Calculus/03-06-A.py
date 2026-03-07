import sys
import numpy as np


def sigmoid(w, x):
    return 1 / (1 + np.exp(x*w))


def main():
    N = int(input())
    train = np.array([list(map(float, input().split())) for _ in range(N)])
    w_0 = float(input())
    
    g = np.sum(train[:, 0] * (sigmoid(w_0, train[:, 0]) - train[:, 1]))
    H = np.sum(train[:, 0]**2 * sigmoid(w_0, train[:, 0]) * (1 - sigmoid(w_0, train[:, 0])))
    
    if H <= 1e-12: 
        print('IMPOSSIBLE')
        return 0
    
    w_1 = w_0 - g/H
    
    print(w_1.round(6))
    
    
if __name__ == '__main__':
    main()