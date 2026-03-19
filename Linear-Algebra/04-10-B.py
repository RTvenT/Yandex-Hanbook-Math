import sys
import numpy as np


def main():
    m = int(input())
    X = np.array([list(map(float, input().split())) for _ in range(m)])
    X_c = X #- X.mean(axis=1, keepdims=True)
    
    C = X_c.T @ X_c / m
    eig_vals, eig_vecs = np.linalg.eig(C)
    
    main_comp = eig_vecs[:, eig_vals.argmax()]
    
    if main_comp[0] < 0: main_comp *= -1
    
    print(*main_comp.round(4), sep=' ')
    
    
if __name__ == '__main__':
    main()