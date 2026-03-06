import sys


def main():
    x, w1, w2, y = map(float, input().split())
    
    ReLU = lambda x: max(0, x)
    
    a = w1*x
    h = ReLU(a)
    y_out = w2*h
    
    dL_dy = y_out - y
    dy_dh = w2 
    dh_da = 1 if a > 0 else 0 
    da_dw1 = x
    
    dL_dw1 = dL_dy * dy_dh * dh_da * da_dw1
    dL_dw2 = dL_dy * h
    
    print(round(dL_dw1, 6), round(dL_dw2, 6))
    
    
if __name__ == '__main__':
    main()
    
    
