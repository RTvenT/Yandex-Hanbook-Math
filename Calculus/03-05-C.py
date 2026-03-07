import sys 
import numpy as np
from numpy import linalg as LA 


def main():
    d, T = map(int, input().split())
    eta, rho, eps = map(float, input().split())
    theta_t = np.array(list(map(float, input().split())))
    
    grads = np.array([list(map(float, input().split())) for _ in range(T)])
    v_t = np.zeros(d)
    
    for t in range(T):   
        v_t = rho * v_t + (1 - rho) * grads[t]**2
        theta_t = theta_t - eta * grads[t] / (np.sqrt(v_t) + eps)
    
    print(*theta_t.round(6), sep=' ')
    
    
if __name__ == '__main__':
    main()