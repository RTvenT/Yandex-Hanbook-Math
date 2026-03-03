import sys


def main():
    print_root = lambda x, i: print(f'Root found: x = {round(x_i, 6)}', f'Number of iterations: {i}', sep='\n')
    a, b, c = map(float, input().split())
    x0 = float(input())
    eps = float(input())

    f = lambda x: a * x**2 + b * x + c
    f_d = lambda x: 2 * a * x + b

    x_i = x0

    

    for i in range(1000):
        if abs(f(x_i)) < eps:
            print_root(x_i, i)
            return
        
        if f_d(x_i) == 0: 
            print('Solution not found')
            return

        x_i = x_i - f(x_i)/f_d(x_i)

    print('Solution not found')


if __name__ == '__main__':
    main()