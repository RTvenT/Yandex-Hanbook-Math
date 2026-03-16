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
        
    return np.array(Q)


def qr(A):
    Q = gram_schmidt(A.T).T
    R = Q.T @ A
    
    return Q, R



def main():
    m, n = map(int, input().split())
    A = np.array([list(map(float, input().split())) for _ in range(m)])
    
    Q, R = qr(A)
    
    for q in Q:
        print(*q, sep=' ')
    for r in R:
        print(*r, sep=' ')
        

if __name__ == '__main__':
    main()