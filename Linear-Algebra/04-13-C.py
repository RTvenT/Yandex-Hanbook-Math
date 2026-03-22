import sys
import numpy as np


def cond(ATA):
    eig_vals = np.linalg.eigvals(ATA)
    lam_max = eig_vals.max()
    lam_min = eig_vals.min()
    
    return lam_max / lam_min if lam_min != 0 else False
    

def main():
    m, n = map(int, input().split())
    X = np.array([input().split() for _ in range(m)]).astype(float)
    
    cond_before = cond(X.T @ X)
    
    mean = X.mean(axis=0, keepdims=True)
    std = X.std(axis=0, keepdims=True)
    
    Z = (X - mean) / np.where(std == 0, 1, std)
    Z[:, std[0] == 0] = 0
    
    cond_after = cond(Z.T @ Z)
    improvement = cond_before / cond_after if cond_before and cond_after else False
    
    print(cond_before.round(4) if cond_before else 'inf', cond_after.round(4) if cond_after else 'inf', improvement.round(4) if improvement else 'nan')
    
    
if __name__ == '__main__':
    main()