import sys
import numpy as np 


def main():
    m, n = map(int, input().split())
    X = np.array([list(map(float, input().split())) for _ in range(m)])
    
    medians = np.median(X, axis=0, keepdims=True)
    Q1 = np.quantile(X, q=0.25, axis=0, keepdims=True)
    Q3 = np.quantile(X, q=0.75, axis=0, keepdims=True)
    IQR = Q3 - Q1
    Z = (X - medians) / np.where(IQR == 0, 1, IQR)
    Z[:, IQR[0] == 0] = 0
    
    for z in Z:
        print(*z.round(4), sep=' ')
    
    
    print(*medians[0].round(4), sep=' ')
    print(*IQR[0].round(4), sep=' ')
    
    
if __name__ == '__main__':
    main()