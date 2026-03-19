import sys
import numpy as np


def main():
    n, d = map(int, input().split())
    X = np.array([list(map(float, input().split())) for _ in range(n)])
    y = np.array(list(map(float, input().split())))
    
    w = np.linalg.inv(X.T @ X) @ X.T @ y.T
    w = w.round(4)
    
    print(*w, sep=' ')
    
    
if __name__ == '__main__':
    main()
    
    