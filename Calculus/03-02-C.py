import sys
import math
from random import uniform


def main():
    e = math.e
    eps = 1e-6   

    f_expr = input()

    f = eval('lambda x, e=e: ' + f_expr)
    a, b = map(float, input().split())

    l_expr = input()
    L = eval(l_expr, {"e": e})


    is_lipschitz = True
    points = [uniform(a, b) for _ in range(10000)]
    points.sort()
    
    for i in range(len(points) - 1):
        x1, x2 = points[i], points[i+1]

        if abs(f(x1) - f(x2)) > abs(x1 - x2) * L + eps:
            is_lipschitz = False
            break

    if is_lipschitz:
        print("LIPSCHITZ")
    else:
        print("NOT LIPSCHITZ")



if __name__ =='__main__':
    main()