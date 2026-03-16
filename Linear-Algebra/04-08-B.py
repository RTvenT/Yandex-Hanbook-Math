import sys
import numpy as np


def main():
    m = int(input())
    
    X = np.array([list(map(float, input().split())) for _ in range(m)])
    y_true = np.array(list(map(float, input().split())))
    
    y_pred = X @ np.linalg.inv(X.T @ X) @ X.T @ y_true
    
    print(*y_pred, sep=' ')
    

if __name__ == '__main__':
    main()