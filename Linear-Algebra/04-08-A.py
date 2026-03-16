import sys
import numpy as np


def gram_schmidt(vecs):
    Q = list()
    V = vecs.copy()
    
    for v in V:
        for q in Q:
            v -= np.dot(v, q) / np.dot(q, q) * q
            
        if not np.allclose(v, np.zeros(v.shape)):
            Q.append(v / np.linalg.norm(v))
        
    return Q


def main():
    k = int(input())
    vecs = np.array([list(map(float, input().split())) for _ in range(k)])
    
    Q = gram_schmidt(vecs)
    
    for q in Q:
        print(*q, sep=' ')
    
    
if __name__ == '__main__':
    main()