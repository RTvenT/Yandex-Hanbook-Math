import sys
import numpy as np


def main():
    m, n, k = map(int, input().split())
    X = np.array([list(map(float, input().split())) for _ in range(m)])
    X = X - X.mean(axis=0)
    U, S, Vt = np.linalg.svd(X, full_matrices=False)

    for i in range(Vt.shape[0]):
        j = np.argmax(np.abs(Vt[i]))
    
        if Vt[i, j] < 0:
            Vt[i] *= -1
            
    Vk = Vt[:k, :].T
    
    Z = X @ Vk

    for row in Z:
        print(*row, sep=' ')
    
    
if __name__ == '__main__':
    main()
    
    
    