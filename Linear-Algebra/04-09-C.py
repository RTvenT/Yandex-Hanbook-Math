import sys
import numpy as np


def main():
    n = int(input())
    A = np.array([list(map(float, input().split())) for _ in range(n)])
    
    eigen_values = np.linalg.eigvals(A).round(4)
    spectral_radius = np.abs(eigen_values).max().round(6)
    
    print(*np.real(eigen_values), sep=' ')
    print(spectral_radius)
    
    
if __name__ == '__main__':
    main()
    