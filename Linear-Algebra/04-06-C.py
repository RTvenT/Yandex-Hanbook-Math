import sys
import numpy as np


def main():
    a1, p, q, r, s, t, u = map(int, input().split())
    a = a1
    b = -(t*q + r*p)
    c = r*u*q + p*s*t - a1*s*u
    
    all_x = np.roots([a, b, c])
    
    if not np.allclose(all_x, all_x.round()):
        print('NO_ROOTS')
    else:
        print(*np.sort(all_x.round().astype(int)), sep=' ')


if __name__ == "__main__":
    main()