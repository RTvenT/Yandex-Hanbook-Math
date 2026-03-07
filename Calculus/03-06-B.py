import sys
import numpy as np


def main():
    a, b, x_prev, x_cur, T = map(float, input().split())
    T = int(T)
    
    f = lambda x: x**4 + a * x**2 + b * x
    fd = lambda x: 4 * x**3 + 2 * a * x + b
    
    if abs(fd(x_cur) - fd(x_prev)) < 1e-12:
            print('FAILED')
            return 0
    
    x_k = x_cur - fd(x_cur) * (x_cur - x_prev) / (fd(x_cur) - fd(x_prev))
    x_prev = x_cur
    
    for k in range(1, T):
        if abs(fd(x_k)) <= 1e-12:
            print(round(x_k, 6))
            return 0
            
        if abs(fd(x_k) - fd(x_prev)) < 1e-12:
            print('FAILED')
            return 0
        
        t = x_k
        x_k = x_k - fd(x_k) * (x_k - x_prev) / (fd(x_k) - fd(x_prev))
        x_prev = t
        
    print(round(x_k, 6))
        
        
if __name__ == '__main__':
    main()