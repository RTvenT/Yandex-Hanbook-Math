import sys
import numpy as np

def main():
    it = iter(sys.stdin.read().split())
    n = int(next(it))
    d = int(next(it))
    
    lam = float(next(it))
    t = float(next(it))
    
    A = []
    b = []
    for _ in range(n):
        row = [float(next(it)) for _ in range(d)]
        bi = float(next(it))
        A.append(row)
        b.append(bi)
    A = np.array(A)
    b = np.array(b)
    
    x0 = np.array([float(next(it)) for _ in range(d)])
    
    grad = A.T @ (A @ x0 - b)
    
    y = x0 - t * grad
    
    x1 = np.sign(y) * np.maximum(np.abs(y) - t * lam, 0)
    x1[np.abs(x1) < 1e-12] = 0.0
    
    Z = np.sum(np.abs(x1) <= 1e-12)
    
    print(*x1.round(6), int(Z))

if __name__ == "__main__":
    main()