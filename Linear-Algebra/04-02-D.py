import sys
import numpy as np


def main():
    n = int(input())
    v1 = np.array(list(map(int, input().split())))
    v2 = np.array(list(map(int, input().split())))
    
    cos = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    angle = np.arccos(cos)
    
    
    print(np.int16(np.rad2deg(angle)))
    
    
if __name__ == '__main__':
    main()