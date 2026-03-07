import sys 
import numpy as np
from numpy import linalg as LA 


def main():
    d, T = map(int, input().split())
    eta, beta1, beta2, eps = map(float, input().split())
    theta_t = np.array(list(map(float, input().split())))
    
    grads = np.array([list(map(float, input().split())) for _ in range(T)])
    m_t = np.zeros(d)
    v_t = np.zeros(d)
     
    for t in range(T):   
        m_t = beta1 * m_t + (1 - beta1) * grads[t]
        v_t = beta2 * v_t + (1 - beta2) * grads[t]**2
        
        m = m_t / (1 - beta1 ** (t+1))
        v = v_t / (1 - beta2 ** (t+1))
        
        theta_t = theta_t - eta * m / (np.sqrt(v) + eps)
    
    print(*theta_t.round(6), sep=' ')
    
    
if __name__ == '__main__':
    main()