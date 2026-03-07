import sys
import numpy as np


def main():
    N, B = map(int, input().split())
    
    grads = np.array(list(map(float, input().split())))
    
    mean_grad = grads.mean()
    var_grad = (N - B)/(B * (N - 1)) * grads.var()
    
    print(mean_grad.round(6), var_grad.round(6))
    
    
if __name__ == '__main__':
    main()