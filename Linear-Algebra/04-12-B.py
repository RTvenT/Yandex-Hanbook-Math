import sys
import numpy as np


def main():
    n, d = map(int, input().split())
    w = np.array(list(map(float, input().split())))
    b = float(input())
    data = np.array([list(map(float, input().split())) for _ in range(n)])
    X_train = data[:, :d]
    y_train = data[:, d].astype(int)
    t = int(input())
    X_test = np.array([list(map(float, input().split())) for _ in range(t)])
    
    norm_w = np.linalg.norm(w)
    
    if np.allclose(norm_w, 0):
        margins = np.zeros(n)
        gamma = 0.0
        supports_vecs = np.zeros(n)
        
        print(gamma)
        print(*supports_vecs.astype(int), sep=' ')
        
        for x in X_test:
            delta = b
            dist = 0.0
            y = int(np.sign(delta)) if not np.allclose(delta, 0) else 1
            
            print(dist, y)
        
        return
    
    
    margins = []
    
    for i in range(n):
        margins.append((np.dot(w, X_train[i]) + b) * y_train[i] / norm_w)
        
    margins = np.array(margins)
    gamma = margins.min()
    
    supports_vecs = np.zeros(n)
    supports_vecs[np.where(margins == gamma)] = 1
    
    print(gamma)
    print(*supports_vecs.astype(int), sep=' ')
    
    for x in X_test:
        delta = np.dot(w, x) + b
        
        dist = abs(delta) / norm_w
        y = int(np.sign(delta)) if not np.allclose(delta, 0) else 1
        
        print(dist.round(4), y)
    
    
if __name__ == '__main__':
    main()