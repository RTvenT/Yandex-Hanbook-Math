import sys 
import numpy as np


def lowrank_approx(A, k):
    A_approx = 0
    U, S, VT = np.linalg.svd(A)
    
    for i in range(min(k, len(S))):
        A_approx += S[i] * np.outer(U[:,i], VT[i,:])
        
    return A_approx
    

def main():
    n, m = map(int, input().split())
    A = np.array([list(map(float, input().split())) for _ in range(n)])
    t = int(input())
    ranks = np.array(list(map(int, input().split())))
    
    for i in ranks:
        k = min(i, n, m)
        A_k = lowrank_approx(A, k)
        relative_error = np.linalg.norm(A - A_k, ord='fro') / np.linalg.norm(A, ord='fro')
        compression_ratio = k * (n + m + 1) / (n*m)
        
        print(relative_error, compression_ratio)
    
    
if __name__ == '__main__':
    main()