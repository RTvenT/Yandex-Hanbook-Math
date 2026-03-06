import sys
import numpy as np
from numpy import linalg as LA 


def closest_to_antigrad(grad, vectors): 
    sim = np.dot(grad, vectors.T)
    return sim.argmin() + 1


def main():
    n, k, eps =  map(float, input().split())
    g = np.array(list(map(float, input().split())))
    V = np.array([list(map(float, input().split())) for _ in range(int(k))])
    V = V / LA.norm(V, axis=1, keepdims=True)
    
    best_idx = closest_to_antigrad(g, V)
    best_v = V[best_idx - 1]
    delta_L = np.dot(g, best_v * eps).round(4)
    
    print(best_idx, delta_L)
    
    
if __name__ == '__main__':
    main()
    

